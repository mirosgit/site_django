from django.conf.urls import re_path, include
from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [

    re_path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    path('basket_adding/', views.basket_adding, name='basket_adding'),
    path('checkout/', views.checkout, name='checkout'),

]