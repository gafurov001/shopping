from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.models import Product, Cart, User


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartModelSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = 'user',


class UserModelSerializer(ModelSerializer):
    confirm_password = CharField(required=True)

    class Meta:
        model = User
        fields = 'username', 'password', 'confirm_password'


