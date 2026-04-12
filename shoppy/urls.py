from django.urls import path
from django.contrib import admin
from .views import hello_world, author, shop,product_info
from . import views

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('author/', author, name='authors' ),
    path('catalog/', shop, name='catalog'),
    path('admin/', admin.site.urls),
    path('catalog/<int:pk>/',product_info, name="product_info" ),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('cart/update/<int:item_id>/', views.cart_update, name='cart_update'),
]