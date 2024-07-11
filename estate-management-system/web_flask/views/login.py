#!/usr/bin/python3
"""
"""

from views import app_view
from flask import Flask, render_template, make_response, request
from flask import session, redirect, url_for, abort
from models import storage
from models.utill import Utill


@app_view.route("/login", methods={"GET", "POST"}, strict_slashes=False)
def login():
    """
    """

    if request.method == "POST":
        data = request.form
        email = data.get("email")
        password = data.get("password")

        user = Utill.is_valid_user(email, password)
        if user is None:
            return render_template(
                        "login.html",
                        f_status="Invalid email or password")

        session["email"] = email
        session["role"] = user.__class__.__name__
        if session["role"] == "Admin":
            return redirect(url_for("app_view.admin"))
        elif session["role"] == "Agent":
            return redirect(url_for("app_view.agent"))
        elif session["role"] == "Tenant":
            return redirect(url_for("app_view.tenant"))


    if request.method == "GET":
        return render_template("login.html")

@app_view.route("/logout", strict_slashes=False)
def logout():
    """ this endpoint is used to logout from user. """

    session.pop("email", None)
    return redirect(url_for("app_view.login"))

