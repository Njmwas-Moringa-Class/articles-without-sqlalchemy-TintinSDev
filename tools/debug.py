#!/usr/bin/env python3
import sys
sys.path.append('lib')  # Assuming 'lib' is one level above 'tools'

import ipdb

from . import Author
from . import Magazine
from . import Article

if __name__ == '__main__':
    #  WRITE YOUR TEST CODE HERE ###
    

    author1 = Author("Peter")
    author2 = Author("Martin")
    
    ipdb.set_trace()
    
    magazine1 = Magazine("Spice Font", "Space World")
    magazine2 = Magazine("Spice FM", "Citizen TV")

    # Insert a breakpoint here to interact with the terminal
    ipdb.set_trace()

    article1 = author1.add_article(magazine1, "The Future of AI")
    article2 = author2.add_article(magazine1, "Coding for Beginners")
    article3 = author1.add_article(magazine2, "Advancements in Space Exploration")

    # Test code
    print("Authors:")
    for author in Author.all():
        print(author.name())

    print("\nMagazines:")
    for magazine in Magazine.all():
        print(f"{magazine.name()} - {magazine.category()}")

    print("\nArticles:")
    for article in Article.all():
        print(f"{article.title()} by {article.author().name()} in {article.magazine().name()}")

    # DO NOT REMOVE THIS
    ipdb.set_trace()

