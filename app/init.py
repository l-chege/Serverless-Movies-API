#main app file initialization

from flask import Flask
from .main import get_movies, get_movies_by_year, get_movie_cover, get_movie_summary

app = Flask(__name__)

#register routes for serveless functions
app.add_url_rule('/api/movies', 'get_movies', get_movies)
app.add_url_rule('/api/movies/year/<int:year>', 'get_movies_by_year', get_movies_by_year)
app.add_url_rule('/api/movies/cover/<string:movie_id>', 'get_movie_cover', get_movie_cover)
app.add_url_rule('/api/movies/summary/<string:movie_id>', 'get_movie_summary', get_movie_summary)