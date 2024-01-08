from django.shortcuts import render

from nlp.forms.forms import CalculatorForm


def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            # Выполнение вычислений или другой обработки входного текста
            output_text = input_text.upper()  # Пример: преобразование в верхний регистр
            form = CalculatorForm(initial={'input_text': input_text, 'output_text': output_text})
    else:
        form = CalculatorForm()
    return render(request, 'calculator.html', {'form': form})