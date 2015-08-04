from flask import Blueprint
from jinja2 import TemplateNotFound

deposit_blueprint = Blueprint(
    'preservation_deposit',
    __name__,
    template_folder='templates',
    static_folder='static',
)

@deposit_blueprint.route('/<depositions:deposition_type>/stats',
                         methods=['GET'])
def show_stats(deposition_type):
    """Render statistical summary of all depositions."""
    try:
        return render_template('stats.html')
    except TemplateNotFound:
        abort(404)
