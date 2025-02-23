from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime
import pytz
import logging

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
logging.basicConfig(level=logging.INFO)


@app.get("/", response_class=HTMLResponse)
async def get_moscow_time(request: Request):
    """Displays the current Moscow time"""
    moscow_timezone = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_timezone).strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Moscow time fetched: {current_time}")
    return templates.TemplateResponse(request, "index.html", {"time": current_time})
