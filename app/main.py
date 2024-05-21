from fastapi.responses import JSONResponse
import pandas as pd
from fastapi import FastAPI
import pymongo, json
from pymongo import MongoClient


app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Whisky-Map",
        "Version": "1.0.0",
    }

def open_conn(
    username = "wilson",
    password = "1234",
    host = "localhost",
    port = 27017,
    db = "",
    table = "",
):
  uri = "mongodb://%s:%s@%s:%s/" % (username, password, host, port)
  conn = pymongo.MongoClient(uri)
  return conn[db][table]

@app.post("/whisky")
async def create_whisky(
    name: str,
    country: str,
    region: str,
    abv: float,
    volume: int,
):
    data = {
        "name": name,
        "country": country,
        "region": region,
        "abv": abv,
        "volume": volume,
    }
    
    collection_whisky = open_conn(db="testdb", table="whisky")
    
    result = collection_whisky.insert_one(data)
    if not result.acknowledged:
        print(f"{name} 寫入失敗！\n")
    
    return JSONResponse(
        content={
            "message": f"{name} 成功寫入資料庫。"
        }
    )
    
@app.get("/whisky")
async def get_whisky():
    collection_whisky = open_conn(db="testdb", table="whisky")
    cursor = collection_whisky.find()
    df_result = pd.DataFrame(list(cursor))
    del df_result['_id']
    
    json_result = df_result.to_json(orient="records")
    
    return json.loads(json_result)
    