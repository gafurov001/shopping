from django.contrib.auth.hashers import make_password
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from apps.models import Product, Cart, User
from apps.serializers import ProductModelSerializer, CartModelSerializer, UserModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


@extend_schema(methods=['PATCH'], exclude=True)
class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CartListCreateAPIView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    permission_classes = IsAuthenticated,

    def post(self, request, **kwargs):
        cart = Cart.objects.create(user_id=request.user.pk, product_id=request.data['product'])
        return Response({'id': cart.pk, 'user': cart.user_id, 'product': cart.product_id})


class CartDestroyAPIView(DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    permission_classes = IsAuthenticated,


@extend_schema(tags=['auth'])
class UserGenericAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def post(self, request):
        data = request.POST
        if data['password'] == data['confirm_password']:
            User.objects.create(username=data['username'], password=make_password(data['password']))
            return Response(HTTP_201_CREATED)
