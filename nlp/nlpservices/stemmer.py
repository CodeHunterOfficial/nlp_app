import nltk
from nltk.stem import PorterStemmer
import spacy

nltk.download('punkt')

class Stemmer:
    def __init__(self, library):
        # Выбор библиотеки для стемминга
        self.library = library
        if library == 'nltk':
            # Использование NLTK для стемминга
            self.stemmer = PorterStemmer()
        elif library == 'spacy':
            # Использование spacy для стемминга
            self.stemmer = spacy.load("en_core_web_sm")
        else:
            # Ошибка, если библиотека не поддерживается
            raise ValueError(f'Unsupported library: {library}')

    def stem(self, text):
        # Стемминг текста
        # Проверка, что текст является строкой и не пустой
        if not isinstance(text, str):
            raise TypeError(f'Expected a string, got {type(text)}')
        if self.library == 'nltk':
            # Использование NLTK для стемминга
            tokens = nltk.word_tokenize(text)
            stems = [self.stemmer.stem(token) for token in tokens]
        elif self.library == 'spacy':
            # Использование spacy для стемминга
            doc = self.stemmer(text)
            stems = [token.lemma_ for token in doc]
        return stems

    def __str__(self):
        # Вывод информации об объекте класса
        return f'Stemmer(library={self.library})'
