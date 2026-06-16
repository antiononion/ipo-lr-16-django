from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    # Исправлено: поле называется 'title', а в шаблоне shop.html ожидается 'cat.name'
    # Добавим свойство name как псевдоним для совместимости с шаблоном
    @property
    def name(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Owner(models.Model):
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='shop/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    numberOF = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return self.title

    def clean(self):
        if self.price is not None and self.price < 0:
            raise ValidationError({'price': 'Цена не может быть отрицательной.'})
        if self.numberOF is not None and self.numberOF < 0:
            raise ValidationError({'numberOF': 'Количество на складе не может быть отрицательным.'})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина пользователя {self.user.username}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Element(models.Model):
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.CASCADE,
        related_name='elements'
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )
    number = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.title} ({self.number} шт.)'

    def cost(self):
        """Стоимость позиции: цена × количество."""
        return self.product.price * self.number

    def clean(self):
        if self.number and self.product and self.number > self.product.numberOF:
            raise ValidationError({
                'number': (
                    f'Нельзя добавить больше '
                    f'{self.product.numberOF} шт. товара «{self.product.title}».'
                )
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Позиция корзины'
        verbose_name_plural = 'Позиции корзины'
        unique_together = ('cart', 'product')
