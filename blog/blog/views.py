import mistune
from flask import render_template
from flask import request, redirect, url_for

from blog import app
from .database import session
from .models import Post

from sqlalchemy import update
from flask import flash
from flask.ext.login import login_user
from flask.ext.login import logout_user
from flask.ext.login import login_required
from werkzeug.security import check_password_hash
from .models import User
from flask.ext.login import current_user

@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    email, password = request.form["email"], request.form["password"]
    user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Incorrect username or password", "danger")
        return redirect(url_for("login_get"))

    login_user(user)
    return redirect(request.args.get('next') or url_for("posts"))

@app.route("/logout")
def logout():
    if current_user.is_authenticated():
        logout_user()
        return render_template("logout.html")
    else:
        return redirect(url_for("login_get"))

@app.route("/")
@app.route("/page/<int:page>")
def posts(page=1, paginate_by=10):
    # Zero-indexed page
    page_index = page - 1
    
    count = session.query(Post).count()

    start = page_index * paginate_by
    end = start + paginate_by

    total_pages = (count - 1) / paginate_by + 1
    has_next = page_index < total_pages - 1
    has_prev = page_index > 0

    posts = session.query(Post)
    posts = posts.order_by(Post.datetime.desc())
    posts = posts[start:end]

    return render_template("posts.html",
        posts=posts,
        has_next=has_next,
        has_prev=has_prev,
        page=page,
        total_pages=total_pages
    )

@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def post(post_id):
    if request.method == "GET":
        post = session.query(Post).filter(Post.id == post_id).first()
        return render_template("post.html", post=post)

    if request.method == "POST" and current_user.is_authenticated():
        post = session.query(Post).filter(Post.id == post_id).first()
        session.delete(post)
        session.commit()
        return redirect(url_for("posts"))

@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    if request.method == "GET":
        post = session.query(Post).filter(Post.id == post_id).first()
        return render_template("edit_post.html", post=post)

    if request.method == "POST":
        post = session.query(Post).filter(Post.id == post_id).first()
        post.title, post.content = request.form["title"], request.form["content"]
        session.add(post)
        session.commit()
        return redirect(url_for("post", post_id=post_id))

@app.route("/post/add", methods=["GET", "POST"])
@login_required
def add_post():
    if request.method == "GET":
        return render_template("add_post.html")

    if request.method == "POST":
        post = Post(
            title=request.form["title"],
            content=mistune.markdown(request.form["content"]),
            author=current_user
        )
        session.add(post)
        session.commit()
        return redirect(url_for("posts"))
