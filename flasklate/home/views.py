from flask import Blueprint, render_template

home = Blueprint(
    "home", 
    __name__,
    template_folder='templates')

@home.route("/")
def home_page():
    return render_template('home/index.html', page_name=home.name)

