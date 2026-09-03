from fastapi.responses import FileResponse


from jarbinlocalapi.main import api


@api.get("/")
def get_root():
    """
        Route: `/api/`

        Simple `Hello World!`
    """
    return {"message": "Hello World!"}
