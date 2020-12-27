from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def index(request):
    context = {
        'title': 'admin',
        'script_link': 'js/auth-admin.js',
        'style_link': 'css/auth-admin.css'
    }

    return render(request, 'adminapp/index.html', context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }

    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_users_create(request):
    if request.method == "POST":
        reg_form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if reg_form.is_valid():
            reg_form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        reg_form = UserAdminRegisterForm()

    context = {
        'style_link': 'css/auth-admin.css',
        'script_link': 'js/auth-admin.js',

        'form': reg_form
    }

    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))

    else:
        form = UserAdminProfileForm(instance=user)

    context = {
        'form': form,
        'user': user
    }

    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()

    return HttpResponseRedirect(reverse('adminapp:admin_users'))


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_users_restore(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()

    return HttpResponseRedirect(reverse('adminapp:admin_users'))
