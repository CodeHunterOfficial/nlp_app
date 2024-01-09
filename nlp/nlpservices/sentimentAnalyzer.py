from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        # Инициализация инструмента для анализа тональности
        self.classifier = pipeline('sentiment-analysis')

    def analyze_sentiment(self, text):
        # Анализ тональности текста
        result = self.classifier(text)
        return result

    def __str__(self):
        # Вывод информации об объекте класса
        return "SentimentAnalyzer using Hugging Face's Transformers for sentiment analysis"