from django.db import models

# Create your models here.

class cars(models.Model):
    id = models.IntegerField(primary_key=True)
    car = models.CharField(max_length=30)
    dicription = models.CharField(max_length=255)
    price = models.CharField(max_length=30)


    class Meta:
        managed = False
        db_table = 'cars'

class tx(models.Model):
    id_TX = models.IntegerField(primary_key=True)
    avto = models.CharField(max_length=30)
    power = models.CharField(max_length=30)
    drive_unit = models.CharField(max_length=30)
    max_speed = models.CharField(max_length=30)
    acceleration = models.CharField(max_length=30)


    class Meta:
        managed = False
        db_table = 'tx'

class user(models.Model):
    id_user = models.IntegerField(primary_key=True)
    FIO = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'user'

class arenda(models.Model):
    id_arenda = models.IntegerField(primary_key=True)
    avtoarenda = models.CharField(max_length=30)
    payment = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    month = models.CharField(max_length=30)
    day = models.CharField(max_length=30)
    timearenda = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'arenda'