from django.shortcuts import render,redirect
from .models import Cart,BookCart,Facture,BookFacture
from product.models import Book
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def getCartCount(request):
    return len(BookCart.objects.filter(cart__user=request.user))

# Create your views here.
@login_required
def getCart(request):
    if request.user.is_authenticated:
        cartItems = []
        for cart_item in BookCart.objects.filter(cart__user=request.user):
            if cart_item.book.discount:
                cartItems.append((cart_item,'{:.2f}'.format(cart_item.book.price *(1 - cart_item.book.discount / 100 ))))
            else:
                cartItems.append((cart_item,cart_item.book.price))

    return render(request,"store/cart.html",{"cart":cartItems})

def deleteItem(request,isbn):
    cart_item = BookCart.objects.get(cart__user=request.user,book=Book.objects.get(ISBN=isbn))
    
    if cart_item.book.quantity == 0 and cart_item.quantity!=0:
        cart_item.book.is_available = True

    cart_item.book.quantity += cart_item.quantity
    cart_item.book.save()

    cart_item.delete()

    return redirect('cart')

@login_required
def addToCart(request,isbn):
    book = Book.objects.get(ISBN=isbn)
    quantity = int(request.POST["quantity"]) if "quantity" in request.POST else 0

    cart = Cart.objects.filter(user=request.user).first()
    
    if not cart:
        cart = Cart.objects.create(user=request.user)
        cart.save()

    try:
        bc = BookCart(cart=cart,book=book,quantity=quantity)
        bc.save()
    except:
        bc = BookCart.objects.get(cart=cart,book=book)
        bc.quantity += quantity
        bc.save()

    # C'est nécéssaire de la decommenter ou la quantity ne change pas avec l'ajout 
    # à la cart
    bc.book.quantity -= quantity
    if bc.book.quantity == 0:
        bc.book.is_available = False

    bc.book.save()

    print(str(cart))

    if request.GET.get('next'):
        response = redirect(request.GET.get('next'))
    else:    
        response = redirect("book",book.slug,book.ISBN)

    response.set_cookie("cart_succes","true",max_age=3)
    return response


def copy_cart_to_facture(cart):
    # Create the facture instance copying relevant fields
    print(cart)
    facture = Facture(user=cart.user)
    facture.save()

    # Copy many-to-many relations using through model
    for book_cart in cart.bookcart_set.all():
        BookFacture.objects.create(
            facture=facture,
            book=book_cart.book,
            quantity=book_cart.quantity
        )

    return facture


def ValidatePurchase(request):
    
    bookcart = BookCart.objects.filter(cart__user=request.user)

    cart = Cart.objects.get(user = request.user)
    copy_cart_to_facture(cart)
    
    for bc in bookcart:    
        if bc.book.quantity == 0:
            bc.book.is_available = False
        bc.book.save()

        # créer la facture

        bc.delete()

    response = redirect("cart")
    response.set_cookie("cart_succes","true",max_age=3)   

    return response

def checkout(request):

    bookcart = BookCart.objects.filter(cart__user=request.user)
    quantities = [int(request.POST[k]) for k in request.POST.keys() if k!="csrfmiddlewaretoken"]

    for bc,quantity in zip(bookcart,quantities):
        if bc.quantity != quantity:
            if quantity == 0:
                bc.delete()
            else : 
                bc.book.quantity += bc.quantity - quantity
                bc.book.save()
                bc.quantity = quantity
                bc.save()

    total = 0
    cartItems = []
    for cart_item in BookCart.objects.filter(cart__user=request.user):
        q = cart_item.quantity
        if cart_item.book.discount:
        
            discount = cart_item.book.discount * cart_item.book.price / 100
            cartItems.append((cart_item,cart_item.book.price - discount ))
            total += (cart_item.book.price - discount) * q
        else:
            cartItems.append((cart_item,cart_item.book.price))
            total += (cart_item.book.price) * q

    context = {
        "cart":cartItems,
        'total':round(total,2)
        }
    
    
    return render(request,"store/checkout.html",context)