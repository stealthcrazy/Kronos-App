from fastapi import FastAPI , Form 
from pydantic import BaseModel
from fastapi import FastAPI 
from typing import Annotated
import psycopg2
import hashlib
import datetime
from fastapi.middleware.cors import CORSMiddleware
import torch
import torch.nn as nn
from Backend.TransformerModel import Transformer
import tiktoken
import os
import random
import asyncio
import time


from Backend.Validation import *
from Backend.ChatMethods import *
from Backend.AuthenticationMethods import*
from Backend.DataFormats import *
from Backend.Model import * 

from fastapi import APIRouter

router = APIRouter(
    prefix="/AuthenticationMethods",
    tags=["AuthenticationMethods"],
)

def AppendSessionToken(user,cur,id):
    token = hashlib.sha256(str(user+str(datetime.datetime.now())).encode("utf-8")).hexdigest()
    
    cur.execute(f"""UPDATE usercredentialtable SET infostatus = 'True' WHERE id = {id};""")




@router.post("/Authcheck")
async def authcheck(id: AuthIDcheck):
    conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="postgres",
    port=5432
    )
    cur = conn.cursor()
    try:
        cur.execute(f"""SELECT infostatus FROM UserCredentialTable WHERE username = '{id.id}' ; """)
        return {"info":cur.fetchone()[0]}
    except:
        return {"info":"False"}