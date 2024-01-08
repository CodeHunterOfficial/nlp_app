from django import forms

class CalculatorForm(forms.Form):
    number1 = forms.FloatField(label='Первое число')
    number2 = forms.FloatField(label='Второе число')
    operation = forms.ChoiceField(
        choices=(
            ('add', '+'),
            ('subtract', '-'),
            ('multiply', '*'),
            ('divide', '/'),
        ),
        widget=forms.Select(), # widget=forms.RadioSelect(),
        label='Выберите операцию'
    )