from rest_framework.test import APITestCase

from django.urls import reverse

from pizza.models import Pizza

from pizza.serializers import PizzaSerializer

from rest_framework import status


class PizzaApiTestCase(APITestCase):
    def test_get_list(self):
        pizza_1 = Pizza.objects.create(name='Гавайская', price=380)
        pizza_2 = Pizza.objects.create(name='Маргарита', price=475)
        pizza_3 = Pizza.objects.create(name='Помидор', price=470)
        pizza_4 = Pizza.objects.create(name='Рим', price=450)

        response = self.client.get(reverse('pizza_api_list'))

        serial_data = PizzaSerializer([pizza_1, pizza_2, pizza_3, pizza_4], many=True).data
        serial_data = {'pizza_list': serial_data}

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serial_data, response.data)

