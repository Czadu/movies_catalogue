from flask import Flask, render_template, request
import csv
import requests

app = Flask(__name__)



@app.route('/')
def homepage():
    movies = [
        {'title' : 'Banana'}, {'title' : 'Mango'}, {'title' : 'Pineapple'}, 
        {'title' : 'Kiwi'}, {'title' : 'Apple'}, {'title' : 'Plump'}, 
        {'title' : 'Carrot'}, {'title' : 'Tomato'}, {'title' : 'Grape'}
    ]
    return render_template("homepage.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)