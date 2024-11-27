from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework.decorators import action
from .serializers import BookSerializer,BookCartSerializer,BookFactureSerializer,GenreSerializer,AccountSerializer
from product.models import Book,Genre
from drf_spectacular.utils import extend_schema
from cart.models import BookCart,BookFacture
from django.conf import settings
from accounts.models import Account
# Create your views here.

class BookViewSet(viewsets.ViewSet):
    queryset = Book.objects.all()

    def get_permissions(self):
        if self.action in ["create","delete"]:
            print(IsAdminUser())
            return [IsAdminUser()]
        else:
            return super().get_permissions()
        
    @extend_schema(responses=BookSerializer)
    def list(self, request):
        serializer = BookSerializer(self.queryset,many = True)
        return Response(serializer.data)
    
    @extend_schema(responses=BookSerializer)
    def retrieve(self,request,pk=None):
        queryset = Book.objects.get(ISBN = pk)
        if not queryset:
             return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = BookSerializer(queryset)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @extend_schema(request=BookSerializer, responses=BookSerializer)
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(responses=None)
    def delete(self, request, pk=None):
        try:
            book = Book.objects.get(ISBN=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

class GenreViewSet(viewsets.ViewSet):
    queryset = Genre.objects.all()

    def get_permissions(self):
        if self.action in ["create","delete"]:
            return [IsAdminUser()]
        else:
            return super().get_permissions()
        
    @extend_schema(responses=GenreSerializer)
    def list(self, request):
        serializer = GenreSerializer(self.queryset,many = True)
        return Response(serializer.data)
    
    @extend_schema(responses=GenreSerializer)
    def retrieve(self,request,pk=None):
        queryset = Genre.objects.get(pk = pk)
        if not queryset:
             return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = GenreSerializer(queryset)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @extend_schema(request=GenreSerializer, responses=GenreSerializer)
    def create(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(responses=None)
    def delete(self, request, pk=None):
        try:
            genre = Genre.objects.get(pk=pk)
            genre.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CartItemsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BookCart.objects.all()
    serializer_class = BookCartSerializer

class FactureItemsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BookFacture.objects.all()
    serializer_class = BookFactureSerializer



class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAdminUser()]
        return [AllowAny()]

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
