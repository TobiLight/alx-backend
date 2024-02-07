#!/usr/bin/env python3
# File: 6-app.py
# Author: Oluwatobiloba Light
"""User user locale"""
from typing import Dict, Union
from flask import Flask, render_template, request, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as: int) -> Union[Dict, None]:
    """Returns a user dictionary or None"""
    if not login_as:
        return None
    return users.get(login_as, None)


@app.before_request
def before_request():
    """Executes before any request"""
    if 'login_as' in request.args:
        user = get_user(int(request.args['login_as']))
        g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Get the best matched language based on the client's accepted languages
    """
    # locale from url params
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in app.config['LANGUAGES']:
            return locale

    # locale from user settings
    user = g.get('user', None)
    user_locale = user.get('locale', None) if user else None
    if user and user_locale in app.config['LANGUAGES']:
        return user_locale

    # locale from request header
    request_locale = request.headers.get('Accept-Language', None)
    if request_locale in app.config['LANGUAGES']:
        return request_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """Index route"""
    return render_template("/6-index.html")


if __name__ == "__main__":
    app.run(debug=True)
