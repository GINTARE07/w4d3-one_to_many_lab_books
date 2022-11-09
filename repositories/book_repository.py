from db.run_sql import run_sql

from models.book import Book

def save(book):
    sql = "INSERT INTO books (name, genre, pages) VALUES (%s, %s, %s) RETURNING *"
    values = [book.name, book.genre, book.pages]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book