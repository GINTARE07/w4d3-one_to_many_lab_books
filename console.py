import pdb

from models.book import Book
from models.author import Author


# import repositories.author_repository as author_repository
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

# book_repository.select_all()

# task_1 = Task("Plant seeds", user1, 30)
# task_repository.save(task_1)

# task_2 = Task("Go for a run", user1, 30, True)
# task_repository.save(task_2)




pdb.set_trace()