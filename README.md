1. Шаблон страницы оформления заказа
html{% extends "base.html" %}
{% block content %}
<form method="post">
  {% csrf_token %}
  <input name="address">
  <button type="submit">Оформить</button>
</form>
{% endblock %}
2. REST API и его принципы
Архитектурный стиль для веб-сервисов. Принципы: stateless (без состояния), единый интерфейс (GET/POST/PUT/DELETE), клиент-сервер, кэшируемость.
3. Установка Django REST Framework
bashpip install djangorestframework
python# settings.py
INSTALLED_APPS = [..., 'rest_framework']
4. Сериализатор в DRF

Преобразует модели Django в JSON и обратно.
pythonclass ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
5. Представление ModelViewSet
pythonfrom rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
6. URL-маршруты через DefaultRouter
pythonfrom rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('products', ProductViewSet)
urlpatterns = router.urls
7. Тестирование в Postman

Создать запрос → указать URL (http://127.0.0.1:8000/api/products/) → выбрать метод (GET/POST/PUT/DELETE) → нажать Send → смотреть ответ.
8. Аутентификация в DRF
python# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
9. Создание, обновление, удаление через API

POST /api/products/ — создать
PUT /api/products/1/ — обновить
DELETE /api/products/1/ — удалить

ModelViewSet делает это автоматически.
10. Связь сериализатора с моделью
pythonclass ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product        # модель
        fields = ['id', 'title', 'price']  # поля
11. Обработка ошибок в API
pythonfrom rest_framework.response import Response
from rest_framework import status

def my_view(request):
    try:
        # логика
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
