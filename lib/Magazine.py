from Article import Article

class Magazine:
    
    magazines = []
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine.magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def add_article(self, author, title):
        new_article = Article(author, self, title)
        self._articles.append(new_article)
        return new_article

    @classmethod
    def all(cls):
        return cls.magazines

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls.magazines if magazine.name() == name), None)

    def article_titles(self):
        return [article.title() for article in self._articles]

    def contributing_authors(self):
        authors = [article.author() for article in self._articles]
        author_count = {author: authors.count(author) for author in authors}
        return [author for author, count in author_count.items() if count > 2]
   
