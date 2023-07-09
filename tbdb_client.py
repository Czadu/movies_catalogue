from flask import Flask, render_template, request
import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MDJkYzBjMjM2ZWZhOTY4M2Q1YzM4N2Q2YWY2OThiZiIsInN1YiI6IjY0NTc5MWYyNmFhOGUwMDBmZjVhNDljZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UGgXYvJYD9OyMF18OnkDxMcrE5bSwRBjdlKms7TS-6U"

app = Flask(__name__)

def get_popular_movies():
        endpoint = "https://api.themoviedb.org/3/movie/popular"
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }
        response = requests.get(endpoint, headers=headers)
        return response.json()

def get_poster_url(poster_api_path, size="w342" ):
        base_url = "https://image.tmdb.org/t/p/"
        return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
        data = get_movies_list(list_type)
        return data["results"][:how_many]


@app.context_processor
def utility_processor():
        def tmdb_image_url(path, size):
            return tmdb_client.get_poster_url(path, size)
        return {"tbdb_image_url": tmdb_image_url}

    ###

def get_single_movie(movie_id):
        endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }
        response = requests.get(endpoint, headers=headers)
        return response.json()


def get_backdrop_url(backdrop_path, size="w780"):
        base_url = "https://image.tmdb.org/t/p/"
        return f"{base_url}{size}{backdrop_path}"

    ### Obsada filmu


def get_single_movie_cast(movie_id):
        endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }
        response = requests.get(endpoint, headers=headers)
        return response.json()["cast"]

def tbdb_image_url(profile_path, size):
        base_url = "https://image.tmdb.org/t/p/"
        return f"{base_url}{size}/{profile_path}"


    ### Wsparcie dla wielu list filmów
'''
def get_movies_list(list_type):
        endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        return response.json()
'''
    ###Kodilla_testy

def call_tbdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_movies_list(list_type):
   return call_tbdb_api(f"movie/{list_type}")