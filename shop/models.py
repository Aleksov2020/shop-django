from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ItemImage(models.Model):
    image = models.ImageField(verbose_name='Изображение товара')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'
