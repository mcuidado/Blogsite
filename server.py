from flask import Flask, render_template, url_for, redirect
import time
from random import randint
from datetime import datetime
import requests
import json
from blog import Blogs

app = Flask(__name__)

blogs = Blogs()

BLOG_DATA = blogs.get_all_blog_data()

FOOTER_DATA = {
    "year":datetime.today().year,
    "name": "Matthew Hippensteel"
}

# url_for("static", filename="style.css")

@app.route("/")
def home():
    return render_template("index.html", data=BLOG_DATA, footer=FOOTER_DATA)

@app.route("/blog")
def read_all_blogs():
    # blog_url = "https://api.npoint.io/e2c3d27dfa84356b27ef"
    return render_template("blogsList.html", data=BLOG_DATA, footer=FOOTER_DATA)

@app.route("/blog/<int:id>")
def read_selected_blog(id):
    return render_template("blogPost.html", blog=BLOG_DATA[id - 1], data=BLOG_DATA, footer=FOOTER_DATA)

@app.route("/about")
def about_me():
    return render_template("about.html", data=BLOG_DATA, footer=FOOTER_DATA)

if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/<path:username>")

# def home(username):
#     return render_template("index.html", 
#         username=username, 
#         random_number=randint(1, 10), 
#         employees=["Johnathan", "Paul", "David"],
#         year=datetime.today().year
#     )



# def decorator_test(function):

#     def wrapper(*args, **kwargs):
#         print("Countdown in ")
#         for i in range(3,0,-1):
#             print(i)
#             time.sleep(1)
#         print("Blast off.")
#         function(*args)
#     return wrapper

# @decorator_test
# def home(text):
#     print(text)
# home("Hello world.")
