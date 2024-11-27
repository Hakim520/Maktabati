from rest_framework import serializers

from product.models import Book,Genre
from cart.models import BookCart,BookFacture
from django.conf import settings
from accounts.models import Account

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class BookCartSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)  # Use existing BookSerializer for nested serialization

    class Meta:
        model = BookCart
        fields = ['id', 'book', 'quantity']


class BookFactureSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)  # Use existing BookSerializer for nested serialization

    class Meta:
        model = BookFacture
        fields = ['id', 'book', 'quantity']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'phone_number', 'is_admin', 'is_active', 'is_staff', 'is_superadmin']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        account = settings.AUTH_USER_MODEL.objects.create_user(**validated_data)
        return account

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password', None))
        return super().update(instance, validated_data)