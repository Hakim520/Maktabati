from django.contrib import admin
from .models import *

# Register your models here.

class FactureAdmin(admin.ModelAdmin):
    list_display=('id_Facture','user')


class BookFactureAdmin(admin.ModelAdmin):
    list_display=('book','quantity','facture')

admin.site.register(Cart)
admin.site.register(BookCart)
admin.site.register(Facture, FactureAdmin)
admin.site.register(BookFacture, BookFactureAdmin)