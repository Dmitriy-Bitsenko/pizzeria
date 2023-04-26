from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=False)
    price = models.FloatField()
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    photo = models.ImageField(upload_to='image%Y/%m/%d', null=False)
    exist = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.name

    class Meta:  # Class for model in admin panel
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'  # Имя для приложения отображения
        ordering = ['name']  # sort fields alphabetically if ['-name']

