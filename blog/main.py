from typing import Optional
from fastapi import FastAPI

from . import database
from . import models
app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)
@app.get("/ping")
def test():
    return {
        "message":"pong"
    }

@app.get("/check")
def check():
    return {
        "message":"health check"
    }
@app.get("/blog")
def blog(id:int=2,check:Optional[str]=None):
    return {"id":id,"check":check}