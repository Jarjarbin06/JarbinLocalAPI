"""
ROOT
"""


from os.path import join
from pathlib import Path
from fastapi import FastAPI
from jinja2 import FileSystemLoader, Environment
from starlette.staticfiles import StaticFiles


JARBINLOCALAPI_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = JARBINLOCALAPI_DIR / "static"


jarbinlocalapi = FastAPI()
jarbinlocalapi.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)


templates = Environment(
    loader=FileSystemLoader(join(STATIC_DIR, "html"))
)
