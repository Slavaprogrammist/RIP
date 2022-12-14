# Generated by Django 4.1.2 on 2022-10-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avto_name', models.CharField(max_length=50, verbose_name='Название автомобиля')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена аренды за час')),
                ('arenda', models.BooleanField(verbose_name='Можно ли арендовать в данный момент?')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Когда последний раз была в аренде?')),
            ],
        ),
    ]
