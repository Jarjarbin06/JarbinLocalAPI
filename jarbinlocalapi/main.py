from jarbinlocalapi.root import jarbinlocalapi as main_app
import uvicorn


#-------------------- RUN --------------------#

def run() -> None:
    uvicorn.run(
        main_app,
        host="0.0.0.0",
        port=8000,
    )

#-------------------- SUB-SYSTEMS --------------------#

from jarbinlocalapi.root import main
from jarbinlocalapi.updater import main
from jarbinlocalapi.api import main
from jarbinlocalapi.app import main
