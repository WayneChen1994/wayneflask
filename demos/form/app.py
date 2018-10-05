#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import os
from flask import Flask, render_template, url_for


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/html', methods=['GET', 'POST'])
def html():
    pass
