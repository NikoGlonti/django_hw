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
    email = forms.EmailField(label='email')
    text = forms.CharField(label='Text', max_length=200)
    date_time = forms.DateTimeField(label='DateTime')

    def clean_date_time(self):
        date_time = self.cleaned_data.get('date_time') - timedelta(hours=2) + timedelta(milliseconds=1)

        if timezone.now() > date_time:
            raise forms.ValidationError("you entered the time in the past")

        if date_time < timezone.now() + timedelta(days=2):
            raise forms.ValidationError("you entered a date more than 2 days old")

        return date_time
