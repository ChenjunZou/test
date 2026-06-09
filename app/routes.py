from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.forms import ContactForm
from app.models import BlogPost, Profile
from app.utils import paginate

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    """Home page with recent blog posts."""
    posts = BlogPost.get_recent(limit=3)
    return render_template("home.html", posts=posts)


@main_bp.route("/about")
def about():
    """About page with profile information."""
    profile = Profile.get_default()
    return render_template("about.html", profile=profile)


@main_bp.route("/blog")
def blog():
    """Blog listing page with pagination."""
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)
    all_posts = BlogPost.get_all()
    paginated = paginate(all_posts, page, per_page)
    return render_template("blog.html", **paginated)


@main_bp.route("/blog/<slug>")
def blog_post(slug):
    """Individual blog post page."""
    post = BlogPost.get_by_slug(slug)
    if post is None:
        return render_template("404.html"), 404
    return render_template("post.html", post=post)


@main_bp.route("/contact", methods=["GET", "POST"])
def contact():
    """Contact form page."""
    form = ContactForm()
    if request.method == "POST":
        form.populate(request.form)
        if form.validate():
            flash("Thank you for your message! I'll get back to you soon.", "success")
            return redirect(url_for("main.contact"))
        flash("Please correct the errors below.", "error")
    return render_template("contact.html", form=form)
