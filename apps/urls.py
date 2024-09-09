from django.urls import path

from apps.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, CartDestroyAPIView, \
    CartListCreateAPIView, UserGenericAPIView

urlpatterns = [
    path('product/', ProductListCreateAPIView.as_view(), name='product_list_create'),
    # GET - получить список всех продуктов.
    # POST - добавить новый продукт.
    path('product/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_detail_update_delete'),
    # GET - получить информацию о конкретном продукте
    # PUT - обновить информацию о продукте.
    # DELETE - удалить продукт.
    path('cart/<int:pk>', CartDestroyAPIView.as_view(), name='cart_delete'),
    # DELETE - удалить объект из корзины.
    path('cart/', CartListCreateAPIView.as_view(), name='cart_list_create'),
    # GET - получить список всех объектoв.
    # POST - добавить новый объект.
    path('user/', UserGenericAPIView.as_view(), name='user_create')
    # POST - для регистрация
]
