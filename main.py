from threading import Thread
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from os import system

def run():
    while True:
        system('python tele_enc.py')
Thread(target=run).start()

app = FastAPI()

@app.get("/")
def home():
    return JSONResponse(content={'status': 'ok'}, status_code=200)

# @app.get("/su")
# def su(cmd: str):
#     system(cmd)
#     return JSONResponse(content={'status': 'ok'}, status_code=200)
