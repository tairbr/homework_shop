# Generated by Django 3.1.7 on 2021-02-27 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('sale', 'Распродажа'), ('popular', 'Популярный')], default=None, max_length=10),
        ),
    ]
