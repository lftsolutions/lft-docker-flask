from flasklate import app
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html', app_name=app.name)