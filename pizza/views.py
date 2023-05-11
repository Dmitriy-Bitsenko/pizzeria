from django.contrib.auth.decorators import permission_required, login_required

from django.utils.decorators import method_decorator

from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, HttpResponseRedirect

from .models import Pizza

from .forms import PizzaForm, RegistrationForm, LoginForm, ContactForm

from django.contrib.auth import login, logout

from django.core.paginator import Paginator

from django.core.mail import send_mail, send_mass_mail

from django.conf import settings

from basket.forms import BasketAddProductForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.http import JsonResponse

from .serializers import PizzaSerializer

from rest_framework import status

from rest_framework.response import Response

from rest_framework.decorators import api_view

from rest_framework import viewsets

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello, you are in the best pizzeria of the world</h1>")


def pizza_list(request):
    pizzas = Pizza.objects.all()
    response = '<h1>Список пицц</h1>'
    for item in pizzas:
        response += f'<div>\n<p>{item.name}</p>\n<p>{item.price}</p></div>'
    return HttpResponse(response)


def index_template(request):
    return render(request, 'pizza/index.html')


def pizza_template(request):
    context = {'title': 'Pizzas'}
    pizzas = Pizza.objects.all()
    paginator = Paginator(pizzas, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)

    context['page_obj'] = page_objects

    if request.method == 'GET':
        pizza_id = request.GET.get('id', 1)
        try:
            pizza_one = Pizza.objects.get(pk=pizza_id)
        except:
            pass
        else:
            context['pizza_one'] = pizza_one
        context['name'] = request.GET.get('name')

    elif request.method == 'POST':
        pizza_id = request.POST.get('id', 1)
        try:
            pizza_one = Pizza.objects.get(pk=pizza_id)
        except:
            pass
        else:
            context['pizza_one'] = pizza_one
        context['name'] = request.POST.get('name')

    return render(
        request=request,
        template_name='pizza/pizza_all.html',
        context=context
    )


@permission_required('pizza.add_pizza')
def pizza_add(request):
    if request.method == 'POST':
        context = dict()
        context['name'] = request.POST.get('name')
        context['description'] = request.POST.get('description')
        context['price'] = request.POST.get('price')
        context['date_create'] = request.POST.get('date_create')
        context['date_update'] = request.POST.get('date_update')
        context['photo'] = request.POST.get('photo')
        context['exist'] = request.POST.get('exist')

        Pizza.objects.create(
            name=context['name'],
            price=context['price'],
            description=context['description'],
            date_create=context['date_create'],
            date_update=context['date_update'],
            photo=context['photo'],
        )
        return HttpResponseRedirect('/pizza/pizza_list/')
    else:
        pizzaform = PizzaForm()
        context = {'form': pizzaform}
    return render(request, 'pizza/pizza_add.html', context=context)


@login_required
def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    basket_form = BasketAddProductForm()

    return render(request, 'pizza/pizza_info.html', {'pizza_item': pizza, 'basket_form': basket_form})


def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect('index_pizza')
    else:
        form = RegistrationForm()
    return render(request, 'pizza/auth/registration.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print('is_anon', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)
            login(request, user)
            print('is_anon', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)
            print(user)
            return redirect('index_pizza')
    else:
        form = LoginForm()
    return render(request, 'pizza/auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('log in')


def contact_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                settings.EMAIL_HOST_USER,
                ['google@google.com'],
                fail_silently=False
            )
            if mail:
                return redirect('index_pizza')
    else:
        form = ContactForm()
    return render(request, 'pizza/email.html', {'form': form})


class PizzaUpdateView(UpdateView):
    model = Pizza
    template_name = 'pizza/pizza_edit.html'
    context_object_name = 'form'
    fields = ['name', 'description', 'price', 'photo']

    @method_decorator(permission_required('pizza.change_pizza'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PizzaDeleteView(DeleteView):
    model = Pizza
    template_name = 'pizza/pizza_delete.html'

    @method_decorator(permission_required('pizza.delete_pizza'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


@api_view(['GET', 'POST'])
def pizza_api_list(request):
    if request.method == 'GET':
        pizza_list = Pizza.objects.all()
        serializer = PizzaSerializer(pizza_list, many=True)
        return Response({'pizza_list': serializer.data})
    elif request.method == 'POST':
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def pizza_api_detail(request, pk, format=None):
    pizza_object = get_object_or_404(Pizza, pk=pk)
    if pizza_object.exist:
        if request.method == 'GET':
            serializer = PizzaSerializer(pizza_object)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = PizzaSerializer(pizza_object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Данные обновлены', 'pizza': serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            pizza_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
