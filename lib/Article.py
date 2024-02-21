class Article:

    articles = []

    def __init__(self, author, magazine, title):

        self._author = author
        self._magazine = magazine
        self._title = title
        self.__class__.articles.append(self)
        magazine.add_published_article(self)
        author._authored_articles(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @classmethod
    def all(cls):
        return cls.articles

