from django.shortcuts import render, get_object_or_404,redirect
from product.models import Book
from django.core.paginator import Paginator
from django.db.models import Count,Case,When,Q,IntegerField,F, FloatField, ExpressionWrapper
from cart.views import getCartCount

# Create your views here.

def store(request):

    url_args = request.META.get('QUERY_STRING', '')
   
    books = Book.objects.all()

    term = request.GET.get("term")
    if term:
        try : 
            term = int(term)
            print(term)
            books_by_isbn = books.filter(ISBN = term)
            if books_by_isbn:
                b = books_by_isbn.first()
                return redirect("book",book_name = b.title,author = b.author,isbn = b.ISBN)
        except:
            pass
        
        #give priority to titles then authors and publishers
        books = books.annotate(
            match_priority=Case(
                When(title__icontains=term, then=1),
                When(author__icontains=term, then=2),
                When(publisher__icontains=term, then=3),
                default=4,
                output_field=IntegerField(),
            )).filter(
                Q(title__icontains=term) |
                Q(author__icontains=term) |
                Q(publisher__icontains=term)
            ).order_by('match_priority', 'title')  # Order primarily by priority, then by title for ties 
        
    genre = request.GET.get("genre")
    if genre:
        books = books.filter(genre__designation = genre)


    formats = request.GET.getlist("forma")
    
    if formats:
        books = books.filter(format__in = formats)

    languages = request.GET.getlist("language")
       
    if languages:
        books = books.filter(language__in = languages)

    


    max = request.GET.get("max")
    if max:
        books = books.annotate(
            discounted_price=ExpressionWrapper(
                F('price') * (1 - F('discount') / 100.0),
                output_field=FloatField()
            )
        ).filter(discounted_price__lte=max)
    else :
        max = 200
    
    min = request.GET.get("min")
    if min:
        books = books.annotate(
            discounted_price=ExpressionWrapper(
                F('price') * (1 - F('discount') / 100.0),
                output_field=FloatField()
            )
        ).filter(discounted_price__gte=min)
    else:
        min = 0
    


    authors_occurences = books.values("author").annotate(c=Count('author')).order_by('-c')

    authors = request.GET.getlist("author")
  
    if authors:
        books = books.filter(author__in = authors)

    format_occurences = books.values("format").annotate(c=Count('format')).order_by('-c')

    language_occurences = books.values("language").annotate(c=Count('language')).order_by('-c')    

    book_count=books.count()
    p = Paginator(books, 6)
    page = request.GET.get('page')
    
    books = p.get_page(page)
    nums = "a" * books.paginator.num_pages

        
    context ={
        "url_args":url_args,
        "nums":nums,
        "authors_count":authors_occurences,
        "formats_count":format_occurences,
        'languages_count':language_occurences,
        'checked_authors':authors,
        'checked_formats':formats,
        'checked_languages':languages,
        'books': books,
        'min':min,
        "max":max,
        'book_count' : book_count
    }

    if term :
        context["search_term"] = term

    if genre :
        context["genre"] = genre

    if 'HX-Request' in request.headers:
        print("inside hx")
        return render(request,"store/store_items.html",context)

    return render(request,'store/store.html', context)


def getBook(request,book_name,isbn):
    b = Book.objects.get(ISBN=isbn)

    return render(request,'store/BookPage.html',{"book":b})

