from threading import Thread
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from os import system
from time import sleep
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

def run():
    tz_vn = ZoneInfo("Asia/Ho_Chi_Minh")
    while True:
        now_vn = datetime.now(tz_vn)
        start_time = datetime.combine(now_vn.date(), time(3, 0), tzinfo=tz_vn)
        end_time = datetime.combine(now_vn.date(), time(4, 0), tzinfo=tz_vn)
        if start_time <= now_vn <= end_time:
            system('python tele_enc.py')
        sleep(3600)
Thread(target=run).start()

app = FastAPI()

@app.get("/")
def home():
    return JSONResponse(content={'status': 'ok'}, status_code=200)

# @app.get("/su")
# def su(cmd: str):
#     system(cmd)
#     return JSONResponse(content={'status': 'ok'}, status_code=200)
