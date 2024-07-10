#!/usr/bin/python3
"""
"""

from views import app_view
from flask import Flask, render_template, make_response, request
from flask import session, redirect, url_for, abort
from models import storage
from models.utill import Utill


@app_view.route("/tenant", strict_slashes=False)
def tenant():
    """
    """

    return("Hellow tenant")

@app_view.route("/add_tenant", strict_slashes=False)
def add_tenant():
    """
    """
