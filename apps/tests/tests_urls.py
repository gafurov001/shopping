import pytest
from django.urls import reverse_lazy
from django.utils.http import urlencode
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED


@pytest.mark.django_db
class TestViews:
    def test_product(self, client, product):
        url = reverse_lazy('product_list_create')
        response = client.get(url)
        assert response.status_code == HTTP_200_OK
        response = response.json()
        assert len(response) == 10
        assert set(response[0]) == {'id', 'name', 'price', 'description', 'stock'}

        response = client.options(url)
        http_methods = response.headers.get('Allow')
        http_methods = set(map(lambda i: i.lower(), http_methods.split(', ')))
        assert http_methods == {'get', 'options', 'head', 'post'}

        response = client.post(url, {'name': 'test1', 'price': 300, 'description': 'test2', 'stock': 55})
        assert response.status_code == HTTP_201_CREATED

