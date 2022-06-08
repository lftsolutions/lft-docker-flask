from flask import Blueprint, render_template


home_blueprint = Blueprint(
    "home", 
    __name__,
    template_folder='templates')


@home_blueprint.route("/")
def home_page():
    return render_template('home/index.html', page_name=home_blueprint.name)

