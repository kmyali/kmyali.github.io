import os
import urllib
from datetime import datetime
from pathlib import Path

from flask import Flask, abort
from flask import render_template

app = Flask(__name__)

@app.route("/")
def about_route():
    return render_template("about.html")

@app.route("/projects/")
def projects_route():
    return render_template("projects.html", projects=projects)


@app.route("/contact/")
def contact_route():
    return render_template("contact.html", api=CONTACT_FORM_ACTION)


if __name__ == "__main__":
    app.run(debug=True)
