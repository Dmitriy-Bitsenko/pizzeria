from django.db import models

from django.urls import reverse


class Pizza(models.Model):
    name = models.CharField(default='pizza', max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.FloatField(default=10, verbose_name='Цена')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата добавления записи')
    date_update = models.DateField(auto_now=True, null=True, verbose_name='Дата обновления записи')
    photo = models.ImageField(upload_to='image%Y/%m/%d', null=True, verbose_name='Фото')
    exist = models.BooleanField(default=True, verbose_name='Существует ли в каталоге?')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list_pizza', kwargs={'one_pizza': self.pk})

    class Meta:  # Class for model in admin panel
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'  # Имя для приложения отображения
        ordering = ['name']  # sort fields alphabetically if ['-name']
