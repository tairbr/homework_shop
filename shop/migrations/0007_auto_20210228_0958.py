# Generated by Django 3.1.7 on 2021-02-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210228_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[(1, 'Распродажа'), (2, 'Популярный'), (3, 'Новинка'), (4, 'Заканчивается'), (5, '')], default=5, max_length=10, verbose_name='Статус'),
        ),
    ]
