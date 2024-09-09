from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, IntegerField, TextField, ForeignKey, CASCADE


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField()
    description = TextField()
    stock = IntegerField()


class User(AbstractUser):
    pass


class Cart(Model):

    user = ForeignKey('apps.User', CASCADE)
    product = ForeignKey('apps.Product', CASCADE)
