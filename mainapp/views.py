from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

def test_context(request):
    context = {
        'title': 'добро пожаловать',
        'username': 'This User',
        'products':[
            {'name':'111', 'price':'222'},
            {'name': '121', 'price': '221'},
            {'name': '112', 'price': '223'}
        ],
        'promotion': True,
        'promotion_products':[
            {'name': '121', 'price': '221'}
        ]
    }
    return render(request, 'mainapp/context.html', context)