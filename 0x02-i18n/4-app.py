#!/usr/bin/env python3
# File: 4-app.py
# Author: Oluwatobiloba Light
"""Flask app with internalization support"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Get the best matched language based on the client's accepted languages
    """
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """Index route"""
    return render_template("/4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
