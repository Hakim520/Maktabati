from django.db import models
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    designation = models.CharField(max_length=30) # scifi, fantasy, romance, fiction, history....
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=255,blank=True)

    
    def __str__(self):
        return (self.designation)
    
    # def get_url(self):
    #     return reverse('book', args=[self.slug])
    

    
class Book(models.Model):

    ISBN = models.IntegerField(unique=True) #ISBN dans notre cas 
    slug=models.SlugField(max_length=200,unique=True)
    image = models.ImageField(upload_to="photos/books")
    title = models.CharField(max_length=30)
    description = models.TextField()
    publicate_date= models.DateField()
    pages = models.IntegerField()
    language = models.CharField(max_length=15,default="english")
    author = models.CharField(max_length=80)
    publisher = models.CharField(max_length=80)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    


    #seller = models.OneToOneField(Seller)
    FORMAT_CHOICES = [
        ('hardcover', 'Hardcover'),
        ('paperback', 'Paperback'),
        ('audio', 'Audio'),
    ]
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)

    genre = models.ManyToManyField(Genre) # manytomany je pense cest mieux...

    is_available=models.BooleanField(default=True)

    on_sale=models.BooleanField(default=False)

    discount=models.IntegerField(default=0)

    def __str__(self):
        return (self.title)
    
    def get_url(self):
        return reverse('book', args=[self.author])
    
    # def get_url(self):
    #     return reverse('book', args=[self.genre.slug,self.slug])
    