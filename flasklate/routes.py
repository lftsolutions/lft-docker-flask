from flasklate import app
from flask import render_template

@app.route("/")
def index():
    project_name = app.root_path.rsplit('/',1)[1].strip()
    return render_template('index.html', project_name=project_name)

@app.route("/greet/<name>")
def greet(name):
    return f"<h1>Hello, {name}!</h1>"