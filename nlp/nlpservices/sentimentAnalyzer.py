from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import tensorflow as tf
from transformers import pipeline

class SentimentAnalysis:
    def __init__(self):
        self.model_name = "cointegrated/rubert-tiny2-cedr-emotion-detection"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = TFAutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.classifier = pipeline('sentiment-analysis', model=self.model, tokenizer=self.tokenizer)

    def analyze_sentiment(self, text):
        #inputs = self.tokenizer(text, return_tensors="tf", padding=True, truncation=True)
        result = self.classifier(text, return_all_scores=True)
        return result