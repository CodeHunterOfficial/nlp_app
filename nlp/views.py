from django.shortcuts import render
from nlp.forms.forms import CalculatorForm
from nlp.nlpservices.tokenizer import Tokenizer
from nlp.nlpservices.lemmatizer import Lemmatizer
from nlp.nlpservices.stemmer import Stemmer

def tokenization(text, library):
    tokenizer = Tokenizer(library)
    tokens = tokenizer.tokenize(text)
    return ', '.join(tokens)  # Возвращаем токены в виде ответа

def lematization(text, library):
    lematizer = Lemmatizer(library)    
    lemmas = lematizer.lemmatize(text)
    return ', '.join(lemmas)  # Возвращаем токены в виде ответа

def stemming(text, library):
    stemmers = Stemmer(library)    
    stems = stemmers.stemmer(text)
    return ', '.join(stems)  # Возвращаем токены в виде ответа

def calculate(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            operation = form.cleaned_data['operation']
            if operation == 'Tokenization':
               output_text = tokenization(input_text, 'transformers')  # Используем библиотеку spacy для токенизации
            elif operation=='Lemmatization':
               output_text = lematization(input_text, 'spacy')
            elif operation=='Stimming':
               output_text = lematization(input_text, 'nltk')  
            else:
                output_text = input_text.upper() + operation  # Пример: преобразование в верхний регистр
            form = CalculatorForm(initial={'input_text': input_text, 'output_text': output_text})
    else:
        form = CalculatorForm()
    return render(request, 'nlptask.html', {'form': form})
