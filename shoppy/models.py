from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    pass

class Category(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Owner(models.Model):
    title = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    photo = models.ImageField(upload_to = 'shop/')
    price = models.DecimalField(max_digits = 10, decimal_places=2)
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
        if self.price < 0:
            raise ValidationError({'price': 'Price cannot be negative'})
        if self.numberOF < 0:
            raise ValidationError({'numberOF': 'Stock quantity cannot be negative'})

class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"Корзина пользователя {self.user.username}"
    
class Element(models.Model):
    cart = models.ForeignKey(
        'Cart',
        on_delete = models.CASCADE,
    )
    product = models.ForeignKey(
        'Product',
        on_delete = models.CASCADE
    )
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.title} ({self.number} шт.)"

    def cost(self):
        return self.product.price * self.number

    def clean(self):
        """
        Проверка, что количество товара в корзине
        не превышает доступное количество на складе.
        """
        if self.number > self.product.numberOF:
            raise ValidationError({
                'количество': (
                    f'Нельзя добавить больше '
                    f'{self.product.numberOF} шт. данного товара.'
                )
            })

    def save(self, *args, **kwargs):
        # гарантируем вызов валидации при сохранении
        self.full_clean()
        super().save(*args, **kwargs)