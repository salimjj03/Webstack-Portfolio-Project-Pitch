#!/usr/bin/python3
"""
"""

from views import app_view
from flask import Flask, render_template, make_response, request
from flask import session, redirect, url_for, abort
from models import storage
from models.utill import Utill
from models.tenant import Tenant


@app_view.route("/tenant", strict_slashes=False)
def tenant():
    """
    """

    return("Hellow tenant")

@app_view.route(
        "/add_tenant",
        methods=["GET", "POST"],
        strict_slashes=False)
def add_tenant():
    """
    """

    if request.method == "GET":
        return render_template("add_tenant.html")

    elif request.method == "POST":
        data = request.form

        status = Utill.is_key_exist(**data)
        if status is not False:
            return render_template("add_tenant.html", f_status=status)

        tenant = Tenant(**data)
        tenant.role = 3
        tenant.save()
        return redirect(url_for("app_view.login"))

