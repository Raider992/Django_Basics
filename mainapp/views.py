from django.shortcuts import render
from django.utils import timezone
from mainapp.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'geek shop',

        'style_link': 'css/index.css',

        'date': timezone.now()

    }

    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    context = {
        'title': 'geek shop - каталог',

        'currency': 'руб.',

        'style_link': 'css/products.css',

        'products': Product.objects.all(),

        'categories': ProductCategory.objects.all()
    }

    return render(request, 'mainapp/products.html', context)
