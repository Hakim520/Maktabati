from django.urls import path
from . import views

urlpatterns = [
    path('', views.getCart,name="cart"),
    path('addToCart/<int:isbn>',views.addToCart,name="addToCart"),
    path('deleteItem/<int:isbn>',views.deleteItem,name="deleteItem"),
    path('validatePurchase/',views.ValidatePurchase,name="validatePurchase"),
    path('checkout/',views.checkout,name = "checkout"),
]