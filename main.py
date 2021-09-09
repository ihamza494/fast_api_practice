from fastapi import FastAPI 

app= FastAPI()

@app.get("/")
def index():
    return {'data' : {'Name':'Hamza IQbal'}}


@app.get("/about")
def index():
    return {'data' : 'This is about Page'}