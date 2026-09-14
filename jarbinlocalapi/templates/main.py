from jinja2 import Environment, FileSystemLoader
from os.path import join

from jarbinlocalapi.root import JARBINLOCALAPI_DIR

TEMPLATES = Environment(loader=FileSystemLoader(join(JARBINLOCALAPI_DIR, "static", "html")))
