from flask import Blueprint

blueprint = Blueprint(
    "invenio_dphep",
    __name__,
    url_prefix="/",
    template_folder="templates",  # where your custom templates will go
    static_folder="static"        # where the assets go
)