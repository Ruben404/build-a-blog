from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:blogpost@localhost:8889/build-a-blog'

app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(15))
    body = db.Column(db.String(300))

    def __init__(title):
        self.title = title


@app.route('/')
def index():
    return redirect('/blog')


@app.route('/blog')
def all_blogs():

    blogs = Blog.query.all()

    return render_template('blog.html', title="Blog")


@app.route('/postblog')
def post_blog():

    return render_template('postblog.html', title="Post-Blog")



if __name__ == '__main__':
    app.run()