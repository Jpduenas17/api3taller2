import requests
import logging.config

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator 

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    response = api3()
    return {"RoleUsers": response }

@app.get("/API3Taller2Roles/{encryptedToken}")
def read_user(encryptedToken : str):
    list=api3()
    for rol in list:
        print(rol)
        if rol["encryptedToken"]==encryptedToken:
            return rol

def api3():
    url='https://62fc67e61e6a530698a5ee17.mockapi.io/API3Taller2Roles'
    response = requests.get(url, {}, timeout=5)
    return response.json()

Instrumentator().instrument(app).expose(app)