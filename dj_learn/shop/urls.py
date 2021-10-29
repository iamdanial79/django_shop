from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.mainpage,name='main'),
    path('product/<slug:product_name>',views.productpage, name='product')

]
