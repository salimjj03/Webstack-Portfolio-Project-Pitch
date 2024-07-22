#!/usr/bin/python3
"""
"""

from views import app_view
from flask import render_template, session, jsonify
from flask import redirect, url_for, request
from models import storage
from models.admin import Admin
from models.agent import Agent
from models.house import House
from models.utill import Utill
import os


@app_view.route("/admin", strict_slashes=False)
def admin():
    """
    """

    if session.get("role") != "Admin":
        return redirect(url_for("app_view.login")) 
    user = storage.find_obj_by_key("Admin", email=session["email"])
    return render_template("admin.html", user=user)


@app_view.route(
        "/admin/add_agent",
        methods=["GET", "POST"],
        strict_slashes=False
        )
def add_agent():
    """
    """
    
    user = storage.find_obj_by_key(
                "Admin",
                email=session["email"]
                )

    if request.method == "GET":
        return render_template("add_agent.html", user=user)

    if request.method == "POST":
        data = request.form

        status = Utill.is_key_exist(**data)
        if status is not False:
            return render_template(
                    "add_agent.html",
                    user=user, f_status=status
                    )
        if data["role"] == "1":
            admin = Admin(**data)
            admin.save()
            status = "{} added successufully".format(admin.full_name)
            return render_template(
                    "add_agent.html",
                    user=user, s_status=status
                    )
        elif data["role"] == "2":
            agent = Agent(**data)
            agent.save()
            status = "{} added successufully".format(agent.full_name)
            return render_template(
                    "add_agent.html",
                    user=user, s_status=status
                    )

@app_view.route(
        "/admin/add_house",
        methods=["GET", "POST"],
        strict_slashes=False
        )
def add_house():
    """
    """

    user = storage.find_obj_by_key(
                "Admin",
                email=session["email"]
                )
    agents = storage.all("Agent")

    if request.method == "GET":
        return render_template(
                "add_house.html",
                user=user,
                agents=agents
                )

    if request.method == "POST":


        if 'file' not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == '':
            return "No selected file"
        if file:
            data = request.form
            house = House(**data)
            house.price = "₦{}".format(house.price)
            house.save()
            filename = "{}.jpg".format(house.id)
            file.save(os.path.join(
                'web_flask/static/uploads/',
                filename
                )
                )
        return render_template(
                "add_house.html",
                user=user,
                agents=agents,
                s_status="House Added successfully"
                )

@app_view.route(
        "/admin/list_agent",
        strict_slashes=False,
        methods=["GET", "POST"]
        )
def list_agent():
    """
    """

    if request.method == "GET":
        agents = storage.all("Agent")
        user = storage.find_obj_by_key(
                "Admin",
                email=session["email"]
                )

        return render_template(
                "list_agent.html",
                agents=agents,
                user=user
                )


@app_view.route(
        "/admin/list_admin",
        strict_slashes=False,
        methods=["GET", "POST"]
        )
def list_admin():
    """
    """

    if request.method == "GET":
        admins = storage.all("Admin")
        user = storage.find_obj_by_key(
                "Admin",
                email=session["email"]
                )

        return render_template(
                "list_admin.html",
                admins=admins,
                user=user
                )

@app_view.route(
        "/admin/list_tenant",
        strict_slashes=False,
        methods=["GET", "POST"]
        )
def list_tenant():
    """
    """

    if request.method == "GET":
        tenants = storage.all("Tenant")
        user = storage.find_obj_by_key(
                "Admin",
                email=session["email"]
                )

        return render_template(
                "list_tenant.html",
                tenants=tenants,
                user=user
                )


@app_view.route(
        "/admin/list_house",
        strict_slashes=False,
        methods=["GET", "POST"]
        )
def list_house():
    """
    """

    if request.method == "GET":
        houses = storage.all("House")
        user = storage.find_obj_by_key(
                "Admin",
                email=session["email"]
                )

        return render_template(
                "list_house.html",
                houses=houses,
                user=user
                )

@app_view.route(
        "/admin/update/<id>",
        strict_slashes=False,
        methods=["POST"]
        )
def update(id):
    """
    """

    print(request.path)
    if request.method == "POST":
        update_key = request.form
        if update_key is None:
            return jsonify("Empty request")
        for cls in ["Admin", "Agent", "Tenant", "House"]:
            obj = storage.find_obj_by_key(
                    cls,
                    id=id
                    )
            if obj is not None:
                response = obj.update(**update_key)
                return jsonify("Update successufully") if response is True else jsonify(request.path)
        return jsonify("Invalid class or id")


@app_view.route(
        "/admin/delete/<id>",
        strict_slashes=False,
        methods=["DELETE"]
        )
def delete(id):
    """
    """

    if request.method == "DELETE":
        update_key = request.get_json()
        if update_key is None:
            return ("Empty request")
        for cls in ["Admin", "Agent", "Tenant", "House", "Occufied_house"]:
            response = storage.delete(cls, id)
            if response is True:
                return "Deleted successufully"
        return("Invalid id")

