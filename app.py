import streamlit as st

from database import (
	add_movie,
	get_all_movies,
	get_average_rating,
	get_genre_summary,
	get_highest_rated_movie,
	initialize_database,
)


st.set_page_config(page_title="Movie Collection Manager")
initialize_database()

st.title("Movie Collection Manager")

st.header("Add Movie")
with st.form("add_movie_form"):
	movie_name = st.text_input("Movie Name")
	genre = st.text_input("Genre")
	rating = st.number_input("Rating", value=0.0, step=0.1)
	release_year = st.number_input(
		"Release Year", value=2000, step=1, format="%d"
	)
	submitted = st.form_submit_button("Add Movie")

if submitted:
	if not movie_name.strip() or not genre.strip():
		st.error("Please enter both a movie name and a genre.")
	else:
		add_movie(
			movie_name.strip(),
			genre.strip(),
			rating,
			int(release_year),
		)
		st.success(f'Added "{movie_name.strip()}" to your collection.')

movies = get_all_movies()

st.header("View Movies")
if movies:
	st.table(
		[
			{
				"Movie ID": movie[0],
				"Movie Name": movie[1],
				"Genre": movie[2],
				"Rating": movie[3],
				"Release Year": movie[4],
			}
			for movie in movies
		]
	)
else:
	st.info("No movies have been added yet.")

st.header("Average Rating")
average_rating = get_average_rating()
if average_rating is None:
	st.write("Add a movie to see the average rating.")
else:
	st.metric("Average rating", f"{average_rating:.2f}")

st.header("Highest Rated Movie")
highest_rated_movie = get_highest_rated_movie()
if highest_rated_movie is None:
	st.write("Add a movie to see the highest-rated movie.")
else:
	_, name, movie_genre, movie_rating, year = highest_rated_movie
	st.write(
		f"**{name}** ({year}) | {movie_genre} | "
		f"Rating: {movie_rating:.2f}"
	)

st.header("Genre-wise Summary")
genre_summary = get_genre_summary()
if genre_summary:
	st.table(
		[
			{"Genre": genre, "Number of Movies": count}
			for genre, count in genre_summary
		]
	)
else:
	st.write("Genre counts will appear here after you add movies.")
