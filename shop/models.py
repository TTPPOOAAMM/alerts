from django.db import models
from django.contrib.auth.models import User  

MAX_LENGTH = 255

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название бренда')
    country = models.CharField(max_length=100, verbose_name='Страна бренда', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Sneakers(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Модель кроссовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.PositiveIntegerField(default=41, verbose_name='Размер')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Цвет')
    photo = models.ImageField(upload_to='sneakers/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_exists = models.BooleanField(default=True, verbose_name='Доступно для заказа')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд')
    category = models.ManyToManyField(Category, verbose_name='Категории')

    def __str__(self):
        return f"{self.brand.name} {self.name} - ({self.price} руб.)"

    class Meta:
        verbose_name = 'Кроссовки'
        verbose_name_plural = 'Кроссовки'

class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"
    TYPE_DELIVERY = [
        (SHOP, 'Вывоз из магазина'),
        (COURIER, 'Курьер'),
        (PICKUPPOINT, 'Пункт выдачи заказов'),
    ] 

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пользователь')
    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия покупателя')
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя покупателя')
    buyer_surname = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Отчество покупателя')
    comment = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Комментарий к заказу')
    delivery_address = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ доставки')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения заказа')
    sneakers = models.ManyToManyField('Sneakers', through='Pos_order', verbose_name='Товары')
    total_price = models.FloatField(default=0.0, verbose_name='Итоговая стоимость')

    def __str__(self):
        return f'#{self.pk} - {self.buyer_firstname} {self.buyer_name} ({self.date_create})'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Pos_order(models.Model):
    sneakers = models.ForeignKey('Sneakers', on_delete=models.PROTECT, verbose_name='Продукт')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество продукта')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на позицию')

    def __str__(self):
        return f'{self.order.pk} {self.sneakers.name} ({self.order.buyer_firstname})'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'

class PersistentMetric(models.Model):
    name = models.CharField(max_length=128, verbose_name="Имя метрики")
    labels = models.CharField(max_length=255, default="", blank=True, verbose_name="Метки")
    value = models.FloatField(default=0.0, verbose_name="Значение")

    class Meta:
        unique_together = ('name', 'labels')
        verbose_name = "Метрика Prometheus"
        verbose_name_plural = "Метрики Prometheus"