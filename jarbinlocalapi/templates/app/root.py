from os.path import join

from jarbinlocalapi.templates.main import TEMPLATES

template_root = TEMPLATES.get_template(join("app", "index.html"))
