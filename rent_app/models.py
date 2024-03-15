from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

status = (('1', 'Рассматривается'), ('0', 'Отклонена'), ('2', 'Одобрена'))

class Renter(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    director = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Директор')
    logo = models.ImageField(upload_to='logos_of_Renters/%Y/%m/%d/', blank=True, null=True, default=f'{settings.MEDIA_URL}defaults/default.png')

    class Meta:
        verbose_name = 'Арендодатель'
        verbose_name_plural = 'Арендодатели'
        ordering = ('-id',)

    def __str__(self):
        return self.title

class Property(models.Model):
    price = models.IntegerField(verbose_name='Цена')
    address = models.TextField(verbose_name='Адрес')
    short_description = models.CharField(max_length=512, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE, verbose_name='Арендодатель', related_name='properties')
    phone_number = models.CharField(max_length=16, verbose_name='Телефон')
    space = models.FloatField(verbose_name='Площадь')
    image = models.ImageField(upload_to='rent-images/%Y/%m/%d/', blank=False, null=False, default=f'{settings.MEDIA_URL}defaults/default.png')

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.renter}_{self.address}'


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,verbose_name='Пользователь')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, verbose_name='Недвижимость')
    name = models.CharField(max_length=128, verbose_name='Имя')
    surname = models.CharField(max_length=128, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=128, blank=True, null=True, verbose_name='Отчество')
    phone_number = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(max_length=128, verbose_name='Электронная почта')
    status = models.CharField(max_length=32, choices=(status), default=1, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата подачи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('-status',)

    def __str__(self):
        return f'Заявка_{self.pk}_от_{self.name}'