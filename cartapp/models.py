from django.db import models

from authapp.models import User
from mainapp.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def sum(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'Корзина для {self.user.first_name}, продукт {self.product.name}'
