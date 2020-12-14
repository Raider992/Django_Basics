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


def products(request):

    context = {
        'title': 'geek shop - каталог',

        'currency': 'руб.',

        'style_link': 'css/products.css',

        'products': Product.objects.all(),

        'categories': ProductCategory.objects.all()
    }

    return render(request, 'mainapp/products.html', context)


def test_context(request):

    context = {

        'title': 'добро пожаловать',

        'username': 'This User',

        'products': [
            {'name': '111', 'price': '222'},
            {'name': '121', 'price': '221'},
            {'name': '112', 'price': '223'}
        ],
        'promotion': True,

        'promotion_products': [
            {'name': '121', 'price': '221'}
        ]
    }

    return render(request, 'mainapp/context.html', context)
