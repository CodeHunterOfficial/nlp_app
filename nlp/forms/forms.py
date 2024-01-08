from django import forms

class CalculatorForm(forms.Form):
    input_text = forms.CharField(label='Исходной текст', widget=forms.Textarea)    
    operation = forms.ChoiceField(
        choices=(   
            # Список операций с ключами на английском и значениями на русском
            ("Tokenization", "Токенизация"),
            ("Lemmatization", "Лемматизация"),
            ("KeywordExtraction", "Выделение ключевых слов"),
            ("PartOfSpeechTagging", "Определение частей речи"),
            ("NamedEntityRecognition", "Разметка именованных сущностей"),
            ("SentimentAnalysis", "Анализ тональности"),
            ("CoreferenceResolution", "Разрешение кореференции"),
            ("MachineTranslation", "Машинный перевод"),
            ("TextGeneration", "Генерация текста")
        ),
        widget=forms.Select(),  # Используем выпадающий список для выбора операции
        label='Выберите операцию'
    )
    output_text = forms.CharField(label='Результат', widget=forms.Textarea, required=False)
