#!/usr/bin/env python3
# File: 2-app.py
# Author: Oluwatobiloba Light
"""Get Locale from request"""

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
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """Index route"""
    return render_template("/2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
