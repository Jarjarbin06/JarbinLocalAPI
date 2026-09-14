from os.path import join

from jarbinlocalapi.templates.main import TEMPLATES

template_doc = TEMPLATES.get_template(join("d", "doc.html"))
