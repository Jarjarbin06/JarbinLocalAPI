from jinja2 import Environment, FileSystemLoader
from os.path import join

from jarbinlocalapi.app import APP_DIR

TEMPLATES = Environment(loader=FileSystemLoader(join(APP_DIR, "static", "html")))
