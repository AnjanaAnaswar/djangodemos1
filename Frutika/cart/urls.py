"""
URL configuration for Frutika project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cart import views
app_name='cart'



urlpatterns = [
    

    path('addtocart/<int:pk>/',views.addto_cart,name='addto_cart'),

    path('cartview/',views.cart_view,name='cart_view'),

    path('cartminus/<int:pk>/',views.cart_minus,name='cart_minus'),

    path('cartdelete/<int:pk>/',views.cart_delete,name='cart_delete'),

    path('placeorder/',views.place_order,name='place_order'),

    path('payment_status/<str:pk>/',views.payment_status,name='payment_status'),

    path('yourorders/',views.your_orders,name='your_orders'),
    

] 




