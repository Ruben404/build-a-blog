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

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/')
def index():
    return redirect('/blog')


@app.route('/blog')
def all_blogs():

    # if request.method == 'POST':
    #     blog_title = request.form('blog')
    #     new_blog = Blog(blog_title, body)
    #     db.session.add(new_blog)
    #     db.session.commit()

    blogs = Blog.query.all()

    return render_template('blog.html', title="Blogs", blogs=blogs)


@app.route('/postblog', methods=['POST', 'GET'])
def post_blog():

    if request.method == 'POST':
        blog_title = request.form['blog-title']
        blog_body = request.form['blog-body']
        new_blog = Blog(blog_title, blog_body)
        db.session.add(new_blog)
        db.session.commit()



    return render_template('postblog.html', title="Post-Blog")



if __name__ == '__main__':
    app.run()