"""
WEB app
"""


from pathlib import Path
from fastapi import APIRouter

from jarbinlocalapi.main import jarbinlocalapi

app = APIRouter(prefix="/app")

jarbinlocalapi.include_router(app)

APP_DIR = Path(__file__).resolve().parents[0]
