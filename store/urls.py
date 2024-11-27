from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<str:book_name>/<int:isbn>/',views.getBook,name='book')
]
 