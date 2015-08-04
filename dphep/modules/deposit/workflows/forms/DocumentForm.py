from wtforms import validators
from invenio.modules.deposit import fields

from .validators.simple_fields import duplicated_doi_validator

class DocumentForm():
    """Document form fields"""

    doi = fields.DOIField(label=_('DOI'),
                          processors=[],
                          export_key='doi',
                          description='e.g. 10.1086/305772 or doi:10.1086/305772',
                          placeholder='',
                          validators=[DOISyntaxValidator("Provided DOI is invalid - it should follow a pattern like: '10.1086/305772'."),
                                      duplicated_doi_validator],
                          )
