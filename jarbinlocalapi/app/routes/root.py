from fastapi.responses import FileResponse


from jarbinlocalapi.main import app
from jarbinlocalapi.app import WEB_DIR


@app.get("/")
def get_root():
    """
        Route: `/app/`

        Simple web `Hello World!`
    """
    return FileResponse(WEB_DIR / "index.html")
