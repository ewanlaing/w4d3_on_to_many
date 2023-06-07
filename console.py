from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Stephen King")
author_repository.save(author1)
author2 = Author("R. L. Stine")
author_repository.save(author2)

book1 = Book("It", author1, "Horror")
book_repository.save(book1)
book2 = Book("Escape From Horrorland", author2, "Horror")
book_repository.save(book2)