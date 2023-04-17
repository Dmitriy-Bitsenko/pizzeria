
from django.urls import path


from pizza.views import *


urlpatterns = [
    path('', index_template),
    path('pizza_list/', pizza_template),
    path('', pizza_list),
    path('pizza_add/', pizza_add),

]
