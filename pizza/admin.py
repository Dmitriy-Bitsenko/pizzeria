from django.contrib import admin

from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'exist')
    list_display_links = ('id', 'name')  # Установка ссылок на атрибуты
    search_fields = ('name', 'price',)
    list_editable = ('price', 'exist',)
    list_filter = ('exist',)


admin.site.register(Pizza, PizzaAdmin)



# Register your models here.
