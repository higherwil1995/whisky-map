from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Whisky-Map",
        "Version": "1.0.0",
    }

@app.get("/home")
def hello_world():
    return {
        "message": "Hello Insta360!",
    }