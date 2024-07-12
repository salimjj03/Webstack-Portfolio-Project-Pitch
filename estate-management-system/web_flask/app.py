#!/usr/bin/python3
"""
"""

from flask import Flask, render_template, make_response, request
from flask import session, redirect, url_for, abort
from views import app_view
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_view)
app.secret_key = "*****"
app.config['UPLOAD_FOLDER'] = 'web_flask/static/uploads/'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/upload/<filenamee>', methods=['POST'])
def upload_file(filenamee):
    if 'file' not in request.files:
        return "No file part"
    file = request.files["file"]
    if file.filename == '':
        return "No selected file"
    if file:
        filename = "{}.jpg".format(filenamee)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('app_view.admin'))

@app.before_request
def befor_request():
    """
    """

    path = ["/admin", "/tenant", "/agent", "/house"]
    for url in path:
        if request.path.startswith(url) and session.get(
                "email"
                ) is None:
            return redirect(url_for("app_view.login"))

@app.errorhandler(404)
def _404(error):
    """
    """

    err = {"error": "Not Found"}
    return make_response(err)

@app.teardown_appcontext
def treardown(exc):
    """ The application context in Flask is typically
    created at the beginning of a request and torn
    down after the request has been handled."""

    storage.close()


if __name__ == "__main__":
    app.run(port=5000, debug=True)
