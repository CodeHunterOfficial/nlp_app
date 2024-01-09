import gensim
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
class WordEmbedding:
    def __init__(self, method):
        # Выбор метода для векторного представления слов
        self.method = method
        if method == 'word2vec':
            # Использование Word2Vec из библиотеки gensim
            self.model = gensim.models.Word2Vec()
        elif method == 'spacy':
            # Использование встроенных векторов слов из библиотеки spaCy
            self.nlp = spacy.load("en_core_web_sm")
        elif method == 'count_vectorizer':
            # Использование CountVectorizer из библиотеки scikit-learn
            self.vectorizer = CountVectorizer()
        elif method == 'tfidf_vectorizer':
            # Использование TfidfVectorizer из библиотеки scikit-learn
            self.vectorizer = TfidfVectorizer()
        else:
            # Ошибка, если метод не поддерживается
            raise ValueError(f'Unsupported method: {method}')

    def vectorize(self, text):
        # Векторное представление слов
        if self.method == 'word2vec':
            # Пример использования Word2Vec для векторизации текста
            vectors = [self.model[word] for word in text.split()]
        elif self.method == 'spacy':
            # Пример использования spaCy для векторизации текста
            doc = self.nlp(text)
            vectors = [token.vector for token in doc]
        elif self.method == 'count_vectorizer' or self.method == 'tfidf_vectorizer':
            # Пример использования CountVectorizer или TfidfVectorizer для векторизации текста
            vectors = self.vectorizer.fit_transform([text]).toarray()
        return vectors

    def __str__(self):
        # Вывод информации об объекте класса
        return f'WordEmbedding(method={self.method})'
