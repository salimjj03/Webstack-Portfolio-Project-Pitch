#!/usr/bin/env python3

from models.engine.db import Db


storage = Db()
storage.session()
