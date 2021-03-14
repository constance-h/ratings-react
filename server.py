"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db
import crud

from jina2 import StrictUndefined

app = Flask(__name__)
app.secret_let = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """View all movies."""

    return render_template('/movies.html')

@app.route('/api/movies/<id>')
def movie(id):
    """View specific movie"""

    movie = crud.get_movie_by_id(id)

    return jsonify({'movie': {'movie_id': movie.movie_id, 'title': movie.title, 'overview': movie.overview, 'release_date': movie.release_date, 'poster_path': movie.poster_path}})

@app.route('/api/movies')
def movies():
    
    movie_list = []
    for movie in crud.get_movies():
        movie_list.append({'movie_id': movie.movie_id, 'title': movie.title, 'overview': movie.overview, 'release_date': movie.release_date, 'poster_path': movie.poster_path})
    return jsonify({'movies': movie_list})
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
