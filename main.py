from flask import Flask, render_template, request
import csv
import requests
import tbdb_client


app = Flask(__name__)




### Stara wersja
"""
@app.route('/')
def homepage():
    movies = tbdb_client.get_movies(how_many=8)
    for movie in movies:
        movie["poster_url"] = tbdb_client.get_poster_url(movie["poster_path"])
        movie["backdrop_url"] = tbdb_client.get_backdrop_url(movie["backdrop_path"])
    return render_template("homepage.html", movies=movies)
"""

### Wersja z wyborem menu

@app.route('/')
def homepage():
    valid_movie_list_types = ['now_playing', 'top_rated', 'upcoming', 'popular']
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in valid_movie_list_types:
        selected_list = 'popular'
    movies = tbdb_client.get_movies(how_many=8, list_type=selected_list)
    for movie in movies:
        movie["poster_url"] = tbdb_client.get_poster_url(movie["poster_path"])
        movie["backdrop_url"] = tbdb_client.get_backdrop_url(movie["backdrop_path"])
    return render_template("homepage.html", movies=movies, current_list=selected_list, movie_list_types=valid_movie_list_types)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tbdb_client.get_single_movie(movie_id)
    backdrop_path = details.get("backdrop_path")
    if backdrop_path:
        backdrop = tbdb_client.get_backdrop_url(backdrop_path)
    else:
        backdrop = None
    cast = tbdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast, backdrop=backdrop)

@app.context_processor
def utility_processor():
    def tbdb_image_url(profile_path, size):
        base_url = "https://image.tmdb.org/t/p/"
        return f"{base_url}{size}/{profile_path}"
    return {"tbdb_image_url": tbdb_image_url}




if __name__ == '__main__':
    app.run(debug=True)

