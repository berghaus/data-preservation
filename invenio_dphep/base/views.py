from flask import Blueprint, render_template, abort
from flask_menu import register_menu
from jinja2 import TemplateNotFound

blueprint = Blueprint(
    "invenio_dphep",
    __name__,
    url_prefix="/",
    template_folder="templates",  # where your custom templates will go
    static_folder="static"        # where the assets go
)

@blueprint.route('/hello')
@register_menu(blueprint, ".hello", "Hello")
def show():
    name = "Frank"
    try:
        return render_template('hello.html', name = name)
    except TemplateNotFound:
        abort(404)
