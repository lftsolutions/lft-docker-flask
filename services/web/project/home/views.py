import logging
from flask import Blueprint, render_template

# Logger Creation
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Log Formatter Creation
formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(process)d:%(thread)d | %(filename)s | %(funcName)s | %(lineno)d | %(message)s')

# Log Stream Handler Creation
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

home_blueprint = Blueprint(
    "home", 
    __name__,
    template_folder='templates')


@home_blueprint.route("/")
def home_page():
    
    return render_template('home/index.html', page_name=home_blueprint.name)

