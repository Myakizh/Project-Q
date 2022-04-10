from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/{pk}")
def get_item(pk: int, q: str = None):
    return {"key": pk, "q": q}