
from django.urls import path

from pizza.views import *


urlpatterns = [
    path('', index_template, name='index_pizza'),
    path('pizza_list/', pizza_template, name='list_pizza'),
    path('', pizza_list),
    path('pizza_add/', pizza_add, name='add_pizza'),
    path('pizza_list/<int:pizza_id>/', pizza_detail, name='one_pizza'),
    path('registration/', user_registration, name='regis'),
    path('login/', user_login, name='log in'),
    path('logout/', user_logout, name='log out'),
    path('email/', contact_email, name='contact_email'),
    path('pizza_edit/<int:pk>/', PizzaUpdateView.as_view(), name='pizza_edit'),
    path('pizza_delete/<int:pk>/', PizzaDeleteView.as_view(), name='pizza_delete'),

]
