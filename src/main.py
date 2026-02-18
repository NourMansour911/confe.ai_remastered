from routes import base
from fastapi import FastAPI


app = FastAPI()

app.include_router(base.base_router)
