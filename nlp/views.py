from django.shortcuts import render
from nlp.forms.forms import CalculatorForm
from nlp.nlpservices.middleware import Middleware

def calculate(request):
    middleware = Middleware()
    # Создаем словарь с библиотеками для каждой операции
    libraries = {
        "Tokenization": ['nltk','spacy','transformers'],
        "Lemmatization": ['nltk','spacy','transformers'],
        "Stemming": ['nltk','spacy','transformers', "SnowballStemmer", "PorterStemmer"],
        "Word2Vec": ['word2vec', 'spacy', 'count_vectorizer', 'tfidf_vectorizer'],
        "NamedEntityRecognition": ["SpaCy", "Stanza", "DeepPavlov"],
        "SyntaxAnalysis": ["SpaCy", "Stanza", "NLTK"],
        "MorphologicalAnalysis": ["Pymorphy2", "SpaCy", "Stanza"],
        "SemanticAnalysis": ["transformers"],
        "PartOfSpeechTagging": ["NLTK", "SpaCy", "Stanza"],
        "SentimentAnalysis": ['transformers',"TextBlob", "VADER", "Flair"],
        "EmotionAnalysis": ['transformers', "NRC", "EmoLex", "Emotion", 'transformers'],
        "KeywordExtraction": ['transformers', "RAKE", "YAKE", "TextRank"],
        "NamedEntityRecognition": ['transformers', "SpaCy", "Stanza", "DeepPavlov"],
        "CoreferenceResolution": ['transformers', "NeuralCoref", "AllenNLP", "HuggingFace"],
        "MachineTranslation": ['transformers'],
        "TextGeneration": ['transformers', "GPT-3", "HuggingFace", "TextBlob"]
    }
    if request.method == 'POST':
        form = CalculatorForm(libraries, request.POST) # Передаем словарь библиотек в форму
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            operation = form.cleaned_data['operation']             
            librarychoice = form.cleaned_data['librarychoice']                 
            library = librarychoice.lower() # Используем выбранную библиотеку вместо жестко заданной
            if operation == 'Tokenization':
                output_text = middleware.tokenization(input_text, library)
            elif operation == 'Lemmatization':
                output_text = middleware.lematization(input_text, library)
            elif operation == 'Stemming':
                output_text = middleware.stemming(input_text, library)
            elif operation == 'Word2Vec':
                output_text = middleware.word2vec(input_text, library) # Используем выбранную библиотеку вместо жестко заданной
            elif operation == 'SentimentAnalysis':
                output_text = middleware.analyze_sentiment(input_text, library)          
            else:
                output_text = input_text.upper()  # Пример: преобразование в верхний регистр                        
            form = CalculatorForm(libraries, initial={'input_text': input_text, 'operation': operation, 'librarychoice': librarychoice, 'output_text': output_text}) # Передаем словарь библиотек в форму
    else:
        form = CalculatorForm(libraries) # Передаем словарь библиотек в форму
    return render(request, 'nlptask.html', {'form': form})
