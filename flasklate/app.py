from flask import redirect, url_for
from flasklate import create_app


app = create_app()


@app.route('/')
def home_page():
    return redirect(url_for('home.index'))