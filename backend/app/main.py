from fastapi import FastAPI

from app.api.routes import hello

app = FastAPI(title="Generator liczb losowych API")

app.include_router(hello.router)
