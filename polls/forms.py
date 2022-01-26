from datetime import timedelta

from django import forms
from django.utils import timezone

from .models import Person


class LegsOfTriangle(forms.Form):
    legs_1 = forms.IntegerField(label='введите значение катета', min_value=1)
    legs_2 = forms.IntegerField(label='введите значение катета', min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']


class TextEmail(forms.Form):
    email = forms.EmailField(label='email', required=True, max_length=100)
    text = forms.CharField(label='Text', required=True, max_length=300)
    date_time = forms.DateTimeField(label='DateTime', required=True, initial=timezone.now())

    def clean_date_time(self):
        date_time = self.cleaned_data['date_time']
        if date_time < timezone.now():
            raise forms.ValidationError('Wrong time')
        if date_time > (timezone.now() + timedelta(days=2)):
            raise forms.ValidationError('Wrong time')

        return date_time
