   1. CRUD: Это 4 базовые операции с данными: Create (.create()), Read (.get(), .filter()), Update (.save()), Delete (.delete()).<br>
   2. URL-маршруты: Настраиваются в файле urls.py с помощью функции path('url/', views.my_view, name='name').<br>
   3. Список с фильтрацией: Используется Product.objects.filter(category=...) в представлении (View), данные передаются в контекст шаблона.<br>
   4. Q-объекты: Позволяют строить сложные запросы с условиями ИЛИ и НЕ. Пример: Product.objects.filter(Q(name__icontains='apple') | Q(description__icontains='apple')).<br>
   5. Шаблоны: Создаются HTML-файлы в папке templates. Данные выводятся через теги {{ variable }} и циклы {% for item in list %}.<br>
   6. Доступ к корзине: Применяется декоратор @login_required к функции-представлению или миксин LoginRequiredMixin к классу.<br>
   7. Добавление с проверкой: Перед сохранением CartItem проверяется условие: if product.stock >= requested_quantity:.<br>
   8. Обновление количества: Через POST-запрос из формы, где вызывается CartItem.objects.filter(...).update(quantity=new_value).<br>
   9. Удаление из корзины: Находится нужный объект и вызывается метод: CartItem.objects.get(id=item_id).delete().<br>
   10. Общая стоимость: Вычисляется через агрегацию или цикл: sum(item.product.price * item.quantity for item in cart.items.all()).<br>
   11. Обработка ошибок: Используется конструкция try-except Product.DoesNotExist или функция-ярлык get_object_or_404(Product, id=id).<br>
   12. Интерфейс администратора: Модели регистрируются в admin.py через admin.site.register(ModelName), после чего CRUD доступен в панели /admin.<br>
   13. @login_required: Это декоратор, который перенаправляет неавторизованного пользователя на страницу логина, если он пытается открыть защищенный URL.<br>
   14. Пагинация: Реализуется встроенным классом Paginator из django.core.paginator, который разбивает QuerySet на страницы.<br>
   15. Связи моделей: Используется ForeignKey. Cart привязывается к User, а CartItem — к Cart и к Product.<br>



