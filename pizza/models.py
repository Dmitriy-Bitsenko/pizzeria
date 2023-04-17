from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=False)
    price = models.FloatField()
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    photo = models.ImageField(upload_to='image%Y/%m/%d', null=False)
    exist = models.BooleanField(default=True, null=True)
