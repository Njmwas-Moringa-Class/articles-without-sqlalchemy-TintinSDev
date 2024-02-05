from . import Article
class Author:
    _all_authors = []
    
    def __init__(self, name):
        self._name = name
        Author._all_authors.append(self)
        self._articles = []
        
    def name(self):
        return self._name

    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set(article.magazine() for article in self._articles))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article
    
    def topic_areas(self):
        return list(set(article.magazine().category() for article in self._articles))

    @classmethod
    def all(cls):
        return cls._all_authors
