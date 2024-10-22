import json
import logging
from typing import Optional

import pandas as pd
import pymongo
from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title="Whisky-map-app",
    summary="""
    為了熟悉、掌握 FastAPI 功能而建立的應用程式，提供威士忌的寄酒資訊管理介面。
    """,
    description="""
    預計開發功能：
    **會員資訊**: 新增、刪除、查詢、修改
    **威士忌資訊**: 新增、刪除、查詢、修改
    **寄酒資訊**: 新增、刪除、查詢、修改
    """,
    version="1.0.0",
)

db_config = {**dotenv_values(".env"), **dotenv_values(".env.example")}


# TODO: model object than ODM to Mongodb.
class Whisky(BaseModel):
    name: str
    country: str
    region: str
    abv: float
    volume: int


class Customer(BaseModel):
    name: str
    phone_number: str
    email: Optional[str]


class Staff(BaseModel):
    name: str


class Record(BaseModel):
    id: int


@app.get("/", tags=["Home"])
def home():
    return {
        "project": "Whisky-Map",
        "Version": "1.0.0",
    }


def open_conn(
    username=db_config["MONGO_INITDB_ROOT_USERNAME"],
    password=db_config["MONGO_INITDB_ROOT_PASSWORD"],
    host="whisky-map-mongodb",
    port=27017,
    db="",
    table="",
):
    uri = "mongodb://%s:%s@%s:%s/" % (username, password, host, port)
    conn = pymongo.MongoClient(uri)
    return conn[db][table]


@app.post("/whiskys", tags=["Whisky"])
async def create_whisky(whisky: Whisky):
    data = whisky.model_dump()

    collection_whisky = open_conn(db="app", table="whisky")

    result = collection_whisky.insert_one(data)
    if not result.acknowledged:
        logging.warning(f"{whisky.name} 寫入失敗！\n")
        print(f"{whisky.name} 寫入失敗！\n")

    return JSONResponse(content={"message": f"{whisky.name} 成功寫入資料庫。"})


@app.get("/whiskys", tags=["Whisky"])
async def get_whisky():
    collection_whisky = open_conn(db="app", table="whisky")
    cursor = collection_whisky.find()
    df_result = pd.DataFrame(list(cursor))

    if df_result.empty:
        return {"message": "whisky data not found."}

    del df_result["_id"]
    json_result = df_result.to_json(orient="records")

    return json.loads(json_result)


@app.post("/customers", tags=["Customer"])
async def create_customer(customer: Customer):
    data = customer.model_dump()

    collection_customer = open_conn(db="app", table="customer")

    result = collection_customer.insert_one(data)
    if not result.acknowledged:
        logging.warning(f"{customer.name} 寫入失敗！\n")
        print(f"{customer.name} 寫入失敗！\n")

    return JSONResponse(content={"message": f"{customer.name} 成功寫入資料庫。"})


@app.get("/customers", tags=["Customer"])
async def get_customer():
    collection_customer = open_conn(db="app", table="customer")
    cursor = collection_customer.find()
    df_result = pd.DataFrame(list(cursor))

    if df_result.empty:
        return {"message": "customer data not found."}

    del df_result["_id"]
    json_result = df_result.to_json(orient="records")

    return json.loads(json_result)

@app.post("/appointments", tags=["Appointment"])
async def create_appointment():
    return {"message": "create appointment."}

@app.get("/appointments", tags=["Appointment"])
async def get_appointment():
    return {"message": "get appointment."}
