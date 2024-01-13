from django import forms

class CalculatorForm(forms.Form):
    input_text = forms.CharField(label='Исходной текст', widget=forms.Textarea)    
    operation = forms.ChoiceField(
        choices=(   
            # Список операций с ключами на английском и значениями на русском
            ("Tokenization", "Токенизация"),
            ("Lemmatization", "Лемматизация"),
            ("Stemming", "Стемминг"),
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
        widget=forms.Select(attrs={'onchange': 'this.form.submit();'}),  # Добавляем атрибут onchange
        label='Выберите операцию'
    )
    librarychoice = forms.ChoiceField(
        choices=(),
        widget=forms.Select(),  # Используем выпадающий список для выбора библиотеки
        label='Выберите библиотеку'
    )
    output_text = forms.CharField(label='Результат', widget=forms.Textarea, required=False)

    def __init__(self, libraries, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Получаем значение поля operation из данных формы
        operation = self.data.get("operation")
        # Если значение не пустое, устанавливаем соответствующие библиотеки для поля librarychoice
        if operation:
            self.fields["librarychoice"].choices = [(lib, lib) for lib in libraries[operation]]
