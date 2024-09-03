import os
import sys

import uvicorn

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Get the absolute path of the directory containing main.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the directory containing main.py to the Python path
sys.path.append(current_dir)

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(current_dir), "templates"))

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)
