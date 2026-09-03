from api.main import app

@app.get("/")
def get_root():
    """
        Route: `/`

        Simple Hello World
    """
    return {"message": "Hello World!"}
