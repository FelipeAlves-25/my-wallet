from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from jinja2 import Environment, FileSystemLoader, select_autoescape

html_env = Environment(
    loader=FileSystemLoader("./public"),
    autoescape=select_autoescape
)

app = FastAPI()

@app.get("/")
async def read_root():
    mainpage = html_env.get_template("index.html")
    return HTMLResponse(content=mainpage, status_code=200)
