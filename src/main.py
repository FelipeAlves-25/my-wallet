from fastapi import FastAPI
from jinja2 import Environment

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
