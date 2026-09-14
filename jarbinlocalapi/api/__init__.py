"""
API
"""


from pathlib import Path
from fastapi import APIRouter

from jarbinlocalapi.root import jarbinlocalapi

api = APIRouter(prefix="/api")

jarbinlocalapi.include_router(api)

API_DIR = Path(__file__).resolve().parents[0]
