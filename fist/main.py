
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def index():
    return {'data' : 'green'}

@app.get("/green/{id}")
def show(id):
    return {'green' : id}

@app.get("/green")
def read_root():
    return FileResponse('fist/green.html')

#uvicorn fist.main:app --reload