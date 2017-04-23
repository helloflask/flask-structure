# -*- coding: utf-8 -*-
from autoapp import app


@app.route('/')
def index():
    return 'Hello, Flask!'
