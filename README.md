В админке добавлены новые модели, которыми можно манипулировать<br>

Контрольные вопросы <br>
1. Какие поля и их типы необходимо добавить в модель "Товар"?<br>
name = CharField(max_length=255)<br>
description = TextField()<br>
price = DecimalField(max_digits=10, decimal_places=2)<br>
stock = PositiveIntegerField()<br>
category = ForeignKey(Category, on_delete=models.CASCADE)<br>
manufacturer = ForeignKey(Manufacturer, on_delete=models.CASCADE)<br>

2. Какой параметр on_delete используется и что он означает?
Используется models.CASCADE.
Это означает: при удалении связанного объекта удаляются и все зависимые записи.

3. Какой метод настраивает строковое представление объекта и как он реализован?
Метод __str__(self).
def __str__(self):
    return self.name

4. Зачем используется MinValueValidator и на какие поля?
Он проверяет, чтобы значение не было меньше минимального.
Применяется к полям price и stock.

5. Как связать модель "Производитель" с моделью "Товар"?
manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
Если удалить производителя, все связанные товары тоже удалятся.

6. Как отфильтровать товары по категории "Электроника"?
Product.objects.filter(category__name="Электроника")

7. Какой метод используется для сортировки по цене по убыванию?
Product.objects.order_by('-price')

8. Что такое объект Q в Django ORM?
Q используется для сложных запросов (OR, AND).
from django.db.models import Q

Product.objects.filter(
    Q(name__icontains="телефон") |
    Q(description__icontains="телефон")
)

9. Как реализовать пагинацию по 10 товаров на странице?
from django.core.paginator import Paginator

paginator = Paginator(products, 10)
page = request.GET.get('page')
products = paginator.get_page(page)

10. Как получить товар по ID с обработкой ошибки?
from django.shortcuts import get_object_or_404

product = get_object_or_404(Product, id=id)

11. Как связать модель "Корзина" с User?
from django.contrib.auth.models import User

user = models.OneToOneField(User, on_delete=models.CASCADE)
Тип связи: OneToOne.

12. Какое поле используется для количества товара?
quantity = models.PositiveIntegerField()
Подходит, потому что количество не может быть отрицательным.

13. Как вычислить общую стоимость корзины?
total = sum(item.get_total_price() for item in cart.items.all())

14. Что произойдет с элементами корзины при удалении корзины?
Они автоматически удалятся благодаря:
cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

15. Какой метод вычисляет стоимость одного элемента корзины?
def get_total_price(self):
    return self.product.price * self.quantity

16. Какие поля и их типы необходимо добавить в модель "Товар"?
•	name = CharField(max_length=255)
•	description = TextField()
•	price = DecimalField(max_digits=10, decimal_places=2)
•	stock = PositiveIntegerField()
•	category = ForeignKey(Category, on_delete=models.CASCADE)
•	manufacturer = ForeignKey(Manufacturer, on_delete=models.CASCADE)

17. Какой параметр on_delete используется?
models.CASCADE — удаляет все связанные записи при удалении родительского объекта.

18. Какой метод используется для строкового представления?
Метод __str__(self).
def __str__(self):
    return self.name

19. Зачем используется MinValueValidator?
Чтобы запретить значения меньше заданного минимума.
Применяется к price и stock.

20. Как связать модель "Производитель" с моделью "Товар"?
manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
Удаление производителя удаляет его товары.

21. Как отфильтровать товары по категории "Электроника"?
Product.objects.filter(category__name="Электроника")

22. Как отсортировать товары по цене по убыванию?
Product.objects.order_by('-price')

23. Что такое объект Q?
Позволяет строить сложные запросы.
Product.objects.filter(
    Q(name__icontains="телефон") |
    Q(description__icontains="телефон")
)

24. Как реализовать пагинацию по 10 товаров?
from django.core.paginator import Paginator

paginator = Paginator(products, 10)
page = request.GET.get('page')
products = paginator.get_page(page)

25. Как получить объект товара по ID с обработкой ошибки?
product = get_object_or_404(Product, id=id)

26. Как связать корзину с User?
user = models.OneToOneField(User, on_delete=models.CASCADE)

27. Какой тип поля используется для количества товара?
quantity = models.PositiveIntegerField()

28. Что произойдет с элементами корзины при удалении корзины?
Все элементы корзины удалятся благодаря on_delete=models.CASCADE.

29. Какой метод вычисляет стоимость элемента корзины?
def get_total_price(self):
    return self.product.price * self.quantity

