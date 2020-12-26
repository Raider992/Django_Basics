from django.urls import path

import cartapp.views as cartapp

app_name = 'cartapp'

urlpatterns = [
    path('add/<int:id_product>/', cartapp.cart_add, name='cart_add'),
    path('clear/', cartapp.cart_clear, name='cart_clear'),
    path('add_item/<int:id_product>/', cartapp.cart_add_item, name='cart_add_item'),
    path('remove_item/<int:id_product>/', cartapp.cart_remove_item, name='cart_remove_item'),
    path('clear_position/<int:id_product>/', cartapp.cart_clear_position, name='cart_clear_position')
]
