from application import app
from model.repository import MovieRepository
from model.entity import Movie

repository = MovieRepository()

@app.route("/api/movies", methods=["GET"])
def list():
    return repository.findAll()

@app.route("/api/movies/<code>", methods=["GET"])
def findById(code):
    return repository.findByCode()

@app.route("/api/movies", methods=["POST"])
def create():
    movie = Movie()
    repository.insert(movie)