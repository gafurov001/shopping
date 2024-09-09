from random import randint

import factory
from django.contrib.auth.hashers import make_password

from apps.models import Product, User, Cart


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('text')

    class Meta:
        model = Product

    @factory.lazy_attribute
    def price(self):
        return randint(10, 20) * 100

    @factory.lazy_attribute
    def stock(self):
        return randint(10, 20) * 10


class UserFactory(factory.django.DjangoModelFactory):
    last_name = factory.Faker('last_name')
    first_name = factory.Faker('first_name')
    password = make_password(str(factory.Faker('random_number')))

    class Meta:
        model = User

    @factory.lazy_attribute
    def username(self):
        return '{}_{}'.format(self.first_name, self.last_name).lower()


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart

    @factory.lazy_attribute
    def user(self):
        return randint(1, 6)

    @factory.lazy_attribute
    def product(self):
        return randint(1, 6)
