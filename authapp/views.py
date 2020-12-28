from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse

from cartapp.models import Cart


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))

    else:
        form = UserLoginForm()

    context = {
        'title': 'авторизация',
        'style_link': 'css/auth-admin.css',
        'script_link': 'js/auth-admin.js',

        'form': form
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    if request.method == "POST":
        reg_form = UserRegisterForm(data=request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        reg_form = UserRegisterForm()

    context = {
        'title': 'регистрация',
        'style_link': 'css/auth-admin.css',
        'script_link': 'js/auth-admin.js',

        'form': reg_form
    }

    return render(request, 'authapp/register.html', context)


def profile(request):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))

    else:
        form = UserProfileForm(instance=request.user)

    carts = Cart.objects.filter(user=request.user)

    context = {
        'title': 'профиль',
        'style_link': 'css/profile.css',

        'carts': carts,

        'form': form
    }

    return render(request, 'authapp/profile.html', context)
