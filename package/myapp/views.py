# -*- coding: utf-8 -*-
from myapp import app


@app.route('/')
def index():
    return 'Hello, Flask!'
