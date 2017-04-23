# -*- coding: utf-8 -*-
from myapp.main import main


@main.route('/')
def index():
    return 'Hello, Flask!'