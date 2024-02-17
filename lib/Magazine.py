
class Magazine:
    
    magazines = []

     def __init__(self, name, category):
        self._name = name
        self._category = category
        self.published_articles = []
        self.__class__.magazines.append(self)
         
    @property
    def name(self):
        return self._name
        
    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def add_article(self, author, title):
        new_article = Article(author, self, title)
        self._articles.append(new_article)
        return new_article
        
    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls.magazines if magazine.name == name), None)
  
    @classmethod
    def article_titles(cls, magazine_name):
        magazine = cls.find_by_name(magazine_name)
        if magazine:
            return [article.title for article in magazine.published_articles]
        else:
            return []

    def contributing_authors(self):
        authors_count = {}
        for article in self.published_articles:
            author = article.author
            authors_count[author] = authors_count.get(author, 0) + 1
        return [author for author, count in authors_count
  
    @classmethod
    def all(cls):
        return cls.magazines
        

 

 


   
