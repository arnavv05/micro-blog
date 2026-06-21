from flask import render_template
from app import app
@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Arnav"}
    posts = [
            {
               "author":{"username": "Flop"}, 
               "body":"Beautiful day in portland!"
            },
            {
                "author":{"username": "John Pork"},
                "body":"The avengers movie was so cool!"
            },
            {   
                "author":{"username": "Fork Spoon"},
                "body":"Am I a spork?"
            }
            ]
    return render_template("index.html", title="Home", user=user, posts=posts)