from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import hello_world, author, shop, product_info
from . import views

urlpatterns = [
    # Главная
    path('', hello_world, name='hello_world'),

    # Страницы
    path('author/', author, name='authors'),
    path('catalog/', shop, name='catalog'),
    path('catalog/<int:pk>/', product_info, name='product_info'),

    # Корзина
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('cart/update/<int:item_id>/', views.cart_update, name='cart_update'),

    # Оформление заказа (Задание 1)
    path('checkout/', views.checkout, name='checkout'),

    # Аутентификация
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
