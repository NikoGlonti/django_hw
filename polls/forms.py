from django import forms
from .models import Person


class LegsOfTriangle(forms.Form):
    legs_1 = forms.IntegerField(label='введите значение катета', min_value=1)
    legs_2 = forms.IntegerField(label='введите значение катета', min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']

