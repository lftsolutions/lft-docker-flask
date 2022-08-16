from flask import Blueprint


home_blueprint = Blueprint(
    "home_blueprint",
    __name__,
    static_folder="static",
    template_folder="templates"
)

from project.home import routes