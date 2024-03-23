"""
This is the main module which is used to configure the project setting.
"""
from fastapi import FastAPI

from app.apis import router
from app.database import BASE, engine

BASE.metadata.create_all(engine)


app = FastAPI(title="Business Base")
app.include_router(router, tags=["Business"])
