from flask import Flask, flash, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-only-change-me"

POSTS = [
    {
        "title": "Welcome to Campus Wire",
        "author": "Alex",
        "body": "A small blog for Free Computer Courses learners.",
    },
]


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=120)])
    content = TextAreaField("Content", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Publish draft")


@app.route("/")
def home():
    return render_template("home.html", posts=POSTS)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/new", methods=["GET", "POST"])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        POSTS.insert(
            0,
            {
                "title": form.title.data,
                "author": "Guest",
                "body": form.content.data,
            },
        )
        flash("Draft saved in memory (no database yet).", "success")
        return redirect(url_for("home"))
    return render_template("new_post.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
