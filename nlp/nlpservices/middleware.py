from nlp.nlpservices import sentimentAnalyzer
from nlp.nlpservices.lemmatizer import Lemmatizer
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
        # Преобразование векторов в строки для объединения
        vects_str = [', '.join(map(str, vector)) for vector in vects]
        return vects_str
    
    @staticmethod
    def analyze_sentiment(text):        
        sentiment_analyzer = sentimentAnalyzer.SentimentAnalysis()
        result = sentiment_analyzer.analyze_sentiment(text)
        formatted_result = "\n".join([f"{item['label']}: {item['score']}" for item in result[0]])
        return formatted_result    
    
