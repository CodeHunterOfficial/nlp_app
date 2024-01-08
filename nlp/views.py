from django.shortcuts import render

from nlp.forms.forms import CalculatorForm


def calculate(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            operation = form.cleaned_data['operation']
            #if operation == 'Tokenization':                         
            output_text = input_text.upper()+operation  # Пример: преобразование в верхний регистр
            form = CalculatorForm(initial={'input_text': input_text, 'output_text': output_text})
    else:
        form = CalculatorForm()
    return render(request, 'nlptask.html', {'form': form})