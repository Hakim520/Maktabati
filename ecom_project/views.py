from django.shortcuts import render,redirect
from product.models import Book
from django.contrib.auth import login
from accounts.models import Account


def home(request):
    books = Book.objects.all().filter(is_available=True,on_sale=True)
    context ={
        'products': books,
    }
    return  render(request,'home.html', context)

def register(request):
    errors = False

    if request.method == "POST":

        form = request.POST
        print(form)

        if form["password1"]==form["password2"]:

            try:
                user = Account.objects.create_user(
                    email=form["Username"],
                    username=form["Username"],
                    first_name=form["First name"],
                    last_name=form["Last name"],
                    password=form["password1"]
                    )

                login(request, user)

                return redirect("store")
            except:
                errors = True
        else:
            errors = True
        
    return render(request,'registration/register.html',{"errors":errors})