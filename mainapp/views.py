from django.shortcuts import render
from django.utils import timezone


# Create your views here.


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

        'style_link': 'css/products.css',

        'products': [
            {
                'link': 'vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': '6 090,00 руб.',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'link': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                'name': 'Синяя куртка The North Face',
                'price': '23 725,00 руб.',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            },
            {
                'link': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': '3 390,00 руб.',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            },
            {
                'link': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                'name': 'Черный рюкзак Nike Heritage',
                'price': '2 340,00 руб.',
                'description': 'Плотная ткань. Легкий материал.'
            },
            {
                'link': 'vendor/img/products/Black-Dr-Martens-shoes.png',
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': '13 590,00 руб.',
                'description': 'Гладкий кожаный верх. Натуральный материал.'
            },
            {
                'link': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': '2 890,00 руб.',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
            }
        ]
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
