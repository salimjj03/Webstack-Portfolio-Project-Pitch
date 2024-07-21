#!/usr/bin/python3
"""
"""

from views import app_view
from flask import render_template
from models import storage


@app_view.route("/", strict_slashes=False)
def index():
    """
    """

    houses = storage.all("House")
    agents = storage.all("Agent")

    return render_template("index.html", houses=houses, agents=agents)
