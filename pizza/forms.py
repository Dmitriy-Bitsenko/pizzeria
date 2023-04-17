from django import forms


class PizzaForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.FloatField()
    date_create = forms.DateField()
    date_update = forms.DateField()
    photo = forms.ImageField()
    #exist = forms.BooleanField()
