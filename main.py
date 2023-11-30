from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

@app.get('/')
def index():
    return {"msg":"Api is Working"}

@app.get('/about')
def about():
    return {"msg":"About Page"}

@app.get('/user/{id}')
def user(id:int,limit:Optional[int]=None):
    if limit is None:
        return {"data":{'id':id}}
    else:
        return {"data":{'id':id,'limit':limit}}

class Request(BaseModel):
     name:str
     age:int
     email:str

@app.post('/')
def index(request:Request):
    return{'data':request}