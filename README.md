1. Аутентификация vs Авторизация

Аутентификация — кто ты? (логин/пароль)
Авторизация — что тебе можно? (права доступа)

2. 401 vs 403

401 — не авторизован (не залогинен)
403 — доступ запрещён (залогинен, но нет прав)

3. Способы аутентификации в Django/DRF

Session (по умолчанию в Django)
Token (DRF)
JWT (djangorestframework-simplejwt)
Basic Auth (логин+пароль в заголовке)

4. JWT и его состав

JSON Web Token — токен из трёх частей:

Header (алгоритм)
Payload (данные пользователя)
Signature (подпись)

Разделены точками: xxxxx.yyyyy.zzzzz
5. CSRF

Защита от межсайтовых запросов. При session auth браузер автоматически шлёт куки — злоумышленник может этим воспользоваться. CSRF-токен подтверждает что запрос идёт с твоего сайта.
6. Инструменты прав в Django

is_staff — доступ к админке
is_superuser — все права
Permissions — права на конкретные действия (add, change, delete)
Groups — группы с набором прав

7. Permissions в DRF
python# глобально в settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated']
}

# или на конкретном ViewSet
class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
8. Пользователь видит только свои записи
pythondef get_queryset(self):
    return Order.objects.filter(user=self.request.user)
9. Безопасное хранение токена

JWT — хранить в httpOnly cookie (недоступен JS, защита от XSS)
Не хранить в localStorage — уязвим к XSS
Session token Django хранит в куках автоматически

10. Личный кабинет интернет-магазина

Обязательные разделы:

Профиль (имя, email, пароль)
История заказов
Текущие заказы / статус доставки
Адреса доставки
Корзина