import pdb

from models.book import Book
from models.author import Author


import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

# task_repository.delete_all()
# user_repository.delete_all()

book1 = Book("Positive thinking", "Self-development", 233)
book_repository.save(book1)
book2 = Book("To the Wild", "Travel", 187)
book_repository.save(book2)
book3 = Book("Christmas tales", "Children", 34)
book_repository.save(book3)
book4 = Book("Speedy Bosh", "CookBook", 121)
book_repository.save(book4)

author1 = Author("Jane Etkins", 4)
author_repository.save(author1)
author2 = Author("Rob Radkins", 11)
author_repository.save(author2)
author3 = Author("July Everson", 1)
author_repository.save(author3)
author4 = Author("Miranda Matthews", 5)
author_repository.save(author4)

# book_repository.select_all()

pdb.set_trace()