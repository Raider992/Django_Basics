from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from adminapp import views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('users/', adminapp.admin_users, name='admin_users'),
    path('users/create', adminapp.admin_users_create, name='admin_users_create'),
    path('users/update/<int:user_id>', adminapp.admin_users_update, name='admin_users_update'),
    path('users/remove/<int:user_id>', adminapp.admin_users_remove, name='admin_users_remove'),
    path('users/restore/<int:user_id>', adminapp.admin_users_restore, name='admin_users_restore')

]
