
from django.urls import path


from pizza.views import *


urlpatterns = [
    path('', index_template, name='index_pizza'),
    path('pizza_list/', pizza_template, name='list_pizza'),
    path('', pizza_list),
    path('pizza_add/', pizza_add, name='add_pizza'),
    path('pizza_list/<int:pizza_id>/', pizza_detail, name='one_pizza'),

]
