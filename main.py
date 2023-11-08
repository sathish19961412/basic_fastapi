from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    return {"msg":"Api is Working"}

@app.get('/about')
def about():
    return {"msg":"About Page"}