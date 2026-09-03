from fastapi import FastAPI
import uvicorn


app = FastAPI()


def run() -> None:
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )


from api.routes import root
