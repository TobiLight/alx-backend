#!/usr/bin/env python3
# File: app.py
# Author: Oluwatobiloba Light
"""Display current time"""
from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


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
def before_request() -> None:
    """Executes before any request"""
    if 'login_as' in request.args:
        user = get_user(int(request.args['login_as']))
        g.user = user
        g.time = get_timezone()


@babel.localeselector
def get_locale() -> str:
    """
    Get the best matched language based on the client's accepted languages
    """
    # locale from url params
    if 'locale' in request.args:
        locale: str = request.args['locale']
        if locale in app.config['LANGUAGES']:
            return locale

    # locale from user settings
    user = g.get('user', None)
    user_locale: str = user.get('locale', None) if user else ''
    if user and user_locale in app.config['LANGUAGES']:
        return user_locale

    # locale from request header
    request_locale: str = request.headers.get('Accept-Language', '')
    if request_locale in app.config['LANGUAGES']:
        return request_locale

    default: str = app.config['BABEL_DEFAULT_LOCALE']
    return default


@babel.timezoneselector
def get_timezone() -> str:
    """Get the preferred timezone from URL parameters or default to UTC"""
    # get timezone from url params
    timezone: str = request.args.get('timezone', '').strip()

    # get timezone from user settings
    if not timezone and g.get('user'):
        timezone = g.user.get('timezone', None)

    try:
        from datetime import datetime
        utc_time = datetime.utcnow()
        tz = pytz.timezone(timezone)
        localized_time = tz.localize(
            utc_time).strftime('%b %d, %Y, %I:%M:%S %p')
        return localized_time
    except UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/")
def index():
    """Index route"""
    return render_template("/index.html")


if __name__ == "__main__":
    app.run(debug=True)
