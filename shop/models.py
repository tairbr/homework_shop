from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.name


class Group_of_goods(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название группы товаров')

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES_PRODUCT = (
        (1, 'Распродажа'),
        (2, 'Популярный'),
        (3, 'Новинка'),
        (4, 'Заканчивается'),
        (5, ''),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Название категории')
    group_of_goods = models.ForeignKey(Group_of_goods, on_delete=models.CASCADE, verbose_name='Название группы товаров')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(blank=True, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(verbose_name='В наличии на складе', default=True)
    status = models.IntegerField(verbose_name='Статус', choices=STATUS_CHOICES_PRODUCT, default=5)

    def __str__(self):
        return self.title


