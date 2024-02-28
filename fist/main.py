
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def index():
    return {'data' : 'green'}

@app.get("/green")
def read_root():
    return FileResponse('fist/green.html')

@app.get("/green/unpublished")
def unpublished():
    return {'data':'all unpublished green..'}

@app.get("/green/{id}")
def show(id : int):
    return {'green' : id}



#uvicorn fist.main:app --reload