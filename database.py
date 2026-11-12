import sqlite3
from contextlib import closing
from pathlib import Path


DATABASE_PATH = Path(__file__).parent / "movies.db"


def initialize_database():
	"""Create the movies table if it does not exist."""
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		with connection:
			connection.execute(
				"""
				CREATE TABLE IF NOT EXISTS movies (
					movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
					movie_name TEXT NOT NULL,
					genre TEXT NOT NULL,
					rating REAL NOT NULL,
					release_year INTEGER NOT NULL
				)
				"""
			)


def add_movie(movie_name, genre, rating, release_year):
	"""Add a movie to the database."""
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		with connection:
			connection.execute(
				"""
				INSERT INTO movies (movie_name, genre, rating, release_year)
				VALUES (?, ?, ?, ?)
				""",
				(movie_name, genre, rating, release_year),
			)


def get_all_movies():
	"""Return all movies ordered by ID."""
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		return connection.execute(
			"""
			SELECT movie_id, movie_name, genre, rating, release_year
			FROM movies
			ORDER BY movie_id
			"""
		).fetchall()


def get_average_rating():
	"""Return the average rating, or None when there are no movies."""
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		return connection.execute(
			"SELECT AVG(rating) FROM movies"
		).fetchone()[0]


def get_highest_rated_movie():
	"""Return the highest-rated movie, or None when there are no movies."""
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		return connection.execute(
			"""
			SELECT movie_id, movie_name, genre, rating, release_year
			FROM movies
			ORDER BY rating DESC, movie_id
			LIMIT 1
			"""
		).fetchone()


def get_genre_summary():
	"""Return the movie count for each genre."""
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		return connection.execute(
			"""
			SELECT genre, COUNT(*)
			FROM movies
			GROUP BY genre
			ORDER BY genre
			"""
		).fetchall()
