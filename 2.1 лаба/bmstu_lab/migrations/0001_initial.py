# Generated by Django 4.1.1 on 2022-10-03 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=30)),
                ('contacts', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'accommodation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_id', models.IntegerField()),
                ('accommodation_id', models.IntegerField()),
                ('dates', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'bookings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'guests',
                'managed': False,
            },
        ),
    ]
