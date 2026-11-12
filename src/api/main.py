from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from ui.renderer import render

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return render("index.html")

@app.get("/favicon.ico")
def favicon():
    pass
