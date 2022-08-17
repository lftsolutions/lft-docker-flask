import logging
from logging.handlers import RotatingFileHandler
from flask import render_template
from project.home import home_blueprint

# Logger Creation
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Log Formatter Creation
formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(process)d:%(thread)d | %(filename)s | %(funcName)s | %(lineno)d | %(message)s')

# Log File Handler Creation
file_handler = RotatingFileHandler(
    "project/logs/app.log",
    maxBytes=1000000,
    backupCount=20
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Log Stream Handler Creation
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


@home_blueprint.route("/")
def home():
    logger.debug("Home Page")
    return render_template('index.html', page_name=home_blueprint.name)