from django import forms
from django.contrib.auth.decorators import permission_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from django.utils.decorators import method_decorator

from django.views.generic import UpdateView

from pizza.models import Pizza


class PizzaForm(forms.Form):
    name = forms.CharField(max_length=50, min_length=2, strip=True, label="Название пиццы")
    description = forms.CharField(max_length=120, min_length=2, strip=True, label="Описание пиццы", widget=forms.Textarea)
    price = forms.IntegerField(label="Цена пиццы")
    date_create = forms.DateField(label="Дата добавления пиццы", widget=forms.SelectDateWidget)
    date_update = forms.DateField(label="Дата обновления пиццы", widget=forms.SelectDateWidget)
    photo = forms.ImageField(required=False, label="Фотография пиццы")


class RegistrationForm(UserCreationForm):  # UserCreationForm   BaseUserCreationForm
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={'class': 'form-control', }),
        min_length=2,
    )
    email = forms.CharField(
        label="email",
        widget=forms.EmailInput(attrs={'class': 'form-control', }),
    )
    password1 = forms.CharField(
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={'class': 'form-control', }),
        min_length=2,
    )
    password = forms.CharField(
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )


class ContactForm(forms.Form):
    subject = forms.CharField(
        label='Заголовок',
        widget=forms.TextInput(
            attrs={'class': 'form-control'},
        )
    )
    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                    'rows': 11, },
        )
    )



