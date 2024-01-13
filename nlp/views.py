from django.shortcuts import render
from nlp.forms.forms import CalculatorForm
from nlp.nlpservices.middleware import Middleware

def calculate(request):
    middleware = Middleware()
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            operation = form.cleaned_data['operation']
            #library = form.cleaned_data['library']
            library='nltk'
            if operation == 'Tokenization':
                output_text = middleware.tokenization(input_text, library)
            elif operation == 'Lemmatization':
                output_text = middleware.lematization(input_text, library)
            elif operation == 'Stimming':
                output_text = middleware.stemming(input_text, library)
            elif operation == 'Word2Vec':
                output_text = middleware.word2vec(input_text, "spacy")  
            elif operation == 'SentimentAnalysis':
                output_text = middleware.analyze_sentiment(input_text)
                print(input_text,output_text)            
            else:
                output_text = input_text.upper()  # Пример: преобразование в верхний регистр
            form = CalculatorForm(initial={'input_text': input_text, 'output_text': output_text})
    else:
        form = CalculatorForm()
    return render(request, 'nlptask.html', {'form': form})
