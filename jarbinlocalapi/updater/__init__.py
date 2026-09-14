"""
UPDATER
"""


from pathlib import Path
from fastapi import APIRouter

from jarbinlocalapi.root import jarbinlocalapi

updater = APIRouter(prefix="/updater")

jarbinlocalapi.include_router(updater)

UPDATER_DIR = Path(__file__).resolve().parents[0]
