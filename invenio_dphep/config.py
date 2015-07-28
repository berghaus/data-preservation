CFG_SITE_LANGS = ["en"]

CFG_SITE_NAME = "Data Preservation"
CFG_SITE_NAME_INTL = {
    "en": CFG_SITE_NAME
}

PACKAGES = [
    "invenio_dphep.base",
    "invenio.modules.*",
    "invenio.base",
]

try:
    from invenio_dphep.instance_config import *
except ImportError:
    pass