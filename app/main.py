from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    mylist = ["https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/UCHCYFG98Z5X1616785960389.jpg", 
    "https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/SNA19YFCCIKH1616785958624.jpg", 
    "https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/AEYD63TLZPEV1616785958802.jpg"]
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