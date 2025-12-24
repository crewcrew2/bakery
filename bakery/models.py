from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)

    login = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)

    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)

    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('none', 'Не выбран'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    password = models.CharField(max_length=50)

    role = models.CharField(max_length=20, default='User')

    def __str__(self):
        return self.login


class Admin(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=20, default='Admin')

    def __str__(self):
        return self.login


class Product(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.name