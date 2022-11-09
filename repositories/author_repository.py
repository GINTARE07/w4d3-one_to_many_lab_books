from db.run_sql import run_sql

from models.author import Author
def save(author):
    sql = "INSERT INTO authors (name, books_published) VALUES (%s, %s) RETURNING *"
    values = [author.name, author.books_published]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author