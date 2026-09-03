from fastapi.responses import FileResponse


from jarbinlocalapi.app import app
from jarbinlocalapi.app import APP_DIR


@app.get("/")
def get_root():
    """
        Route: `/app/`

        Simple web `Hello World!`
    """
    return FileResponse(APP_DIR / "index.html")
