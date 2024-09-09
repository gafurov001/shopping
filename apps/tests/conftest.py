import pytest

from apps.tests.factories import UserFactory, ProductFactory, CartFactory


@pytest.fixture()
def user():
    return UserFactory.create_batch(10)


@pytest.fixture()
def product():
    return ProductFactory.create_batch(10)


@pytest.fixture()
def cart():
    return CartFactory.create_batch(10)
