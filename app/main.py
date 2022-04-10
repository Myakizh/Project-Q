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
  
    mylist = []
#    for url in cur.execute('SELECT image FROM winners'):
#        mylist.append(url)
#        print(url)

    url = "('https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/UCHCYFG98Z5X1616785960389.jpg',)"
    for i in range(3):
        mylist.append(url)

    data = {
        "page": "Home page",
        "slider": mylist
        }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = {
        "page": page_name
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})