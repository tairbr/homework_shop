# Generated by Django 3.1.7 on 2021-02-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210227_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('sale', 'Распродажа'), ('popular', 'Популярный'), ('new', 'Новинка'), ('ends', 'Заканчивается'), ('None', '')], default=None, max_length=10, verbose_name='Статус'),
        ),
    ]
