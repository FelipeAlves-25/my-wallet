from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from pathlib import Path
from ui.renderer import render

main_dir = Path(__file__).parent

app = FastAPI()
app.mount("/assets", StaticFiles(directory=main_dir / "ui" / "styles"), name = "assets")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return render(request)


@app.get("/favicon.ico")
def favicon():
    pass
