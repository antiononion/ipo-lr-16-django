from django.urls import path
from django.contrib import admin
from .views import hello_world, author, shop

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('author/', author, name='authors' ),
    path('shop/', shop, name='shop'),
    path('admin/', admin.site.urls),
]