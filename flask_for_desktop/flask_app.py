#! /usr/bin/env python3
# -*- coding : utf-8 -*-

import os
from flask import (
    Flask,
    request,
    render_template,
    flash,
    session,
    url_for,
    redirect
    )


app = Flask(__name__)
app.secret_key = "find_a_better_key!"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5050, debug=True)
