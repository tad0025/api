from threading import Thread
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from os import system
from time import sleep
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from requests import get, post

def render():
    get('https://datt32285.onrender.com')

def rio():
    url = 'https://account.riokupon.com/api/account.php'
    json = {'tp': 'account', 'account_action': 'checkin'}
    head = {'Cookie': 'ckid=5c2f42da2ce8b4b142c6be070e810f79; _ga=GA1.1.1588722211.1709280361; _gcl_au=1.1.535975060.1709280361; us_id=65b6a7031bcf3d4ef7d0873ad85fa5ef; sender_id=5281428451959436; _fbp=fb.1.1709280410687.1686590426; PHPSESSID=2sbhlejm16nfha66l87o2atsdf; _ga_C69QL9B2DF=GS1.1.1709280360.1.1.1709280464.0.0.0'}
    
    while datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")).minute < 57:
        sleep(10)
    
    while True:
        try:
            if datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")).minute == 2:
                break
            print(post(url=url, headers=head, json=json).text)
        except: pass

def run():
    tz_vn = ZoneInfo("Asia/Ho_Chi_Minh")
    tele_enc = datetime.now(tz_vn).replace(hour=3, minute=0, second=0, microsecond=0)
    while True:
        try:
            now_vn = datetime.now(tz_vn)

            if now_vn >= tele_enc:
                Thread(target=system, args=('python tele_enc.py',)).start()
                tele_enc = now_vn + timedelta(days=1)

            if now_vn.hour == 23 and now_vn.minute > 52:
                for i in range(15):
                    Thread(target=rio).start()

            Thread(target=render).start()
            sleep(300)
        except: pass
    
Thread(target=run).start()

app = FastAPI()

@app.get("/")
def home():
    # return JSONResponse(content={'status': 'ok'}, status_code=200)
    pass

# @app.get("/su")
# def su(cmd: str):
#     system(cmd)
#     return JSONResponse(content={'status': 'ok'}, status_code=200)
