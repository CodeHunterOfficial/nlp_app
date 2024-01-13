from django import forms

class CalculatorForm(forms.Form):
    input_text = forms.CharField(label='Исходной текст', widget=forms.Textarea)    
    operation = forms.ChoiceField(
        choices=(   
            # Список операций с ключами на английском и значениями на русском
            ("Tokenization", "Токенизация"),
            ("Lemmatization", "Лемматизация"),
            ("Stimming", "Стимминг"),
            ("Word2Vec", "Векторное представление слов"),
            ("NamedEntityRecognition", "Анализ сущностей"),
            ("SyntaxAnalysis", "Анализ синтаксиса"),
            ("MorphologicalAnalysis", "Анализ морфологии"),
            ("SemanticAnalysis", "Анализ семантики"),
            ("PartOfSpeechTagging", "Определение частей речи"),
            ("SentimentAnalysis", "Анализ тональности"),
            ("EmotionAnalysis", "Анализ эмоций"),         
            ("KeywordExtraction", "Выделение ключевых слов"), 
            ("NamedEntityRecognition", "Разметка именованных сущностей"),
            ("CoreferenceResolution", "Разрешение кореференции"),
            ("MachineTranslation", "Машинный перевод"),
            ("TextGeneration", "Генерация текста")
        ),
        widget=forms.Select(),  # Используем выпадающий список для выбора операции
        label='Выберите операцию'
    )
    output_text = forms.CharField(label='Результат', widget=forms.Textarea, required=False)
