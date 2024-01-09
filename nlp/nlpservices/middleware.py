from nlp.nlpservices.lemmatizer import Lemmatizer
from nlp.nlpservices.sentimentAnalyzer import SentimentAnalyzer
from nlp.nlpservices.stemmer import Stemmer
from nlp.nlpservices.tokenizer import Tokenizer
from nlp.nlpservices.wordEmbedding import WordEmbedding

class Middleware:
    @staticmethod
    def tokenization(text, library):
        tokenizer = Tokenizer(library)
        tokens = tokenizer.tokenize(text)
        return ', '.join(tokens)

    @staticmethod
    def lematization(text, library):
        lemmatizer = Lemmatizer(library)
        lemmas = lemmatizer.lemmatize(text)
        return ', '.join(lemmas)

    @staticmethod
    def stemming(text, library):
        stemmer = Stemmer(library)
        stems = stemmer.stem(text)
        return ', '.join(stems)
    
    @staticmethod
    def word2vec(text, library):
        vectors = WordEmbedding(library)
        vects = vectors.vectorize(text)
        return ', '.join(vects)
    
    @staticmethod
    def analyze_sentiment(text):
        sentiments = SentimentAnalyzer()
        sents = sentiments.analyze_sentiment(text)
        return ', '.join(sents)
    
