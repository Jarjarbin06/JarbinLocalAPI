from jarbinlocalapi.api import api


@api.get("/")
def get_root():
    """
        Route: `/api/`

        Simple `Hello World!`
    """
    return {"message": "Hello World!"}
