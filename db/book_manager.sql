DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  genre VARCHAR(255),
  pages INT
);

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  books_published INT
--   user_id INT NOT NULL REFERENCES users(id)
);