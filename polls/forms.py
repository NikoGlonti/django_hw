from django import forms


class LegsOfTriangle(forms.Form):
    legs_1 = forms.FloatField(label='введите значение катета', min_value=1)
    legs_2 = forms.FloatField(label='введите значение катета', min_value=1)
