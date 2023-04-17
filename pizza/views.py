from django.shortcuts import render

from django.http import HttpResponse

from .models import Pizza

from .forms import PizzaForm


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

    context['pizza_list'] = pizzas

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

    # context = {
    #     'title': 'Pizzas',
    #     'pizza_list': pizzas,
    #     'pizza_one': pizza_one,
    #     'name': name,
    # }

    return render(
        request=request,
        template_name='pizza/pizza_all.html',
        context=context
    )


def pizza_add(request):
    if request.method == 'POST':
        context = dict()
        context['name'] = request.POST.get('name')
        context['description'] = request.POST.get('description')
        context['date_create'] = request.POST.get('date_create')
        context['date_update'] = request.POST.get('name')
        context['photo'] = request.POST.get('date_update')
        context['exist'] = request.POST.get('exist')
        return render(request, 'pizza/pizza_info.html', context=context)
    else:
        pizzaform = PizzaForm()
        context = {'form': PizzaForm}
    return render(request, 'pizza/pizza_add.html', context=context)