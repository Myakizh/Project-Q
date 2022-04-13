from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3

con = sqlite3.connect('D:/byak/Project Q/blizzard_scraper/blizzard_scraper/spiders/base.db')
cur = con.cursor()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
  
    people = []
    titles = []
    uni = []
    images = []
    for url in cur.execute('SELECT * FROM winners'):
        people.append(url[0])
        titles.append(url[1])
        uni.append(url[2])
        images.append(url[3])

    data = {
        "page": "Home page",
        "people": people,
        "titles": titles,
        "uni": uni,
        "slider": images,
        }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = {
        "page": page_name
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})