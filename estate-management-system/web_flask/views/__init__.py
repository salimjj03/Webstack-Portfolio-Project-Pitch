#!/usr/bin/python3
"""
"""

from flask import Flask, Blueprint
import os


app_view = Blueprint("app_view", __name__)


from views.admin import *
from views.agent import *
from views.tenant import *
from views.login import *
from views.house import *
from views.index import *

