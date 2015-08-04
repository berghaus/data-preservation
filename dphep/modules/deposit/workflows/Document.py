"""Workflow for Document"""

from __future__ import absolute_import, print_function
from invenio.modules.deposit.types import SimpleRecordDeposition

class document(SimpleRecordDeposition):
    """"A document containing descriptions to provide context to the site or
    other records in the library."""
    name = _("Document")
