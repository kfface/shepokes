from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('hello', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template("hello.html")

@bp.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html")

@bp.route('/', methods=['GET'])
def index():
    return render_template("hello.html")