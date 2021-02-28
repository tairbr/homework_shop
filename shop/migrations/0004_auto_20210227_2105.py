# Generated by Django 3.1.7 on 2021-02-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210227_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='В наличии на складе'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('sale', 'Распродажа'), ('popular', 'Популярный'), ('new', 'Новинка'), ('None', '')], default=None, max_length=10, verbose_name='Статус'),
        ),
    ]
