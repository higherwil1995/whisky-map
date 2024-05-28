from fastapi.responses import JSONResponse
import pandas as pd
from fastapi import FastAPI
import pymongo, json, logging
from pymongo import MongoClient
# from config import config

# logging.basicConfig(filename="/app/logs/whisky-map.log", level=logging.INFO)

app = FastAPI(
    title="Whisky-map-app",
    description="""
    為了熟悉、掌握 FastAPI 功能而建立的應用程式，提供威士忌的資訊管理介面。
    """,
    version="1.0.0",
)
    

@app.get("/")
def home():
    return {
        "project": "Whisky-Map",
        "Version": "1.0.0",
    }

def open_conn(
    username = "root",
    password = "root",
    host = "whisky-map-mongodb",
    port = 27017,
    db = "",
    table = "",
):
  uri = "mongodb://%s:%s@%s:%s/" % (username, password, host, port)
  conn = pymongo.MongoClient(uri)
  return conn[db][table]

@app.post("/whiskys")
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
    
    collection_whisky = open_conn(db="app", table="whisky")
    
    result = collection_whisky.insert_one(data)
    if not result.acknowledged:
        logging.warning(f"{name} 寫入失敗！\n")
        print(f"{name} 寫入失敗！\n")
    
    return JSONResponse(
        content={
            "message": f"{name} 成功寫入資料庫。"
        }
    )
    
@app.get("/whiskys")
async def get_whisky():
    collection_whisky = open_conn(db="app", table="whisky")
    cursor = collection_whisky.find()
    df_result = pd.DataFrame(list(cursor))
    
    if df_result.empty:
        return {"message": "whisky data not found."}
    
    del df_result['_id']
    json_result = df_result.to_json(orient="records")
    
    return json.loads(json_result)
    