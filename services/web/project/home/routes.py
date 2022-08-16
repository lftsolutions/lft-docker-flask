from flask import render_template
from project.home import home_blueprint

@home_blueprint.route("/")
def home_page():
    return render_template('index.html', page_name=home_blueprint.name)