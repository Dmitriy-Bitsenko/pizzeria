from django import forms


class PizzaForm(forms.Form):
    name = forms.CharField(max_length=50, min_length=2, strip=True, label="Название пиццы")
    description = forms.CharField(max_length=120, min_length=2, strip=True, label="Описание пиццы", widget=forms.Textarea)
    price = forms.IntegerField(label="Цена пиццы")
    date_create = forms.DateField(label="Дата добавления пиццы", widget=forms.SelectDateWidget)
    date_update = forms.DateField(label="Дата обновления пиццы", widget=forms.SelectDateWidget)
    photo = forms.ImageField(required=False, label="Фотография пиццы")
