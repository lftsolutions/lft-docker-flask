from flask import Flask, redirect, url_for
app = Flask(__name__)

from flasklate.home.views import home
app.register_blueprint(home)

@app.route('/')
def home_page():
    return redirect(url_for('home.index'))