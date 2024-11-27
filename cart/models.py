from django.db import models

# Create your models here.

from product.models import Book
from django.conf import settings
# Create your models here.

class Cart(models.Model):
    id_cart = models.AutoField(primary_key=True)
    book = models.ManyToManyField(Book,through="BookCart")

    # si on utilise une autre classe pour User, on changera que `User`
    # car, ca probablement on va heriter du `class User` de Django
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}:{','.join([b.title for b in self.book.all()])}"
    
# pour avoir la quantité d'un livre dans un cart donnée
class BookCart(models.Model):
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['cart','book'], name="unique_book_in_cart")
        ]

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class Facture(models.Model):
    id_Facture = models.AutoField(primary_key=True)
    book = models.ManyToManyField(Book,through="BookFacture")

    # si on utilise une autre classe pour User, on changera que `User`
    # car, ca probablement on va heriter du `class User` de Django
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_Facture}:{self.user}"
    
# pour avoir la quantité d'un livre dans un Facture donnée
class BookFacture(models.Model):
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['facture','book'], name="unique_book_in_Facture")
        ]

    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return f" facture {self.facture.id_Facture}"