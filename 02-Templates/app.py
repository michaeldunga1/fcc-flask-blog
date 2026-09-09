from flask import Flask, render_template

app = Flask(__name__)

POSTS = [
    {
        "title": "Welcome to Campus Wire",
        "author": "Alex",
        "body": "A small blog for Free Computer Courses learners.",
    },
    {
        "title": "Why Flask?",
        "author": "Jordan",
        "body": "Flask stays out of your way until you need more structure.",
    },
]


@app.route("/")
def home():
    return render_template("home.html", posts=POSTS)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
