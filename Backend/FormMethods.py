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




from Backend.AuthenticationMethods import*
from Backend.DataFormats import *


from fastapi import APIRouter

router = APIRouter(
    prefix="/FormMethods",
    tags=["FormMethods"],
)




@router.post("/Login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    #print(password,username)


    
    conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="postgres",
    port=5432
    )
    cur = conn.cursor()
    cur.execute(f""" SELECT EXISTS (SELECT password FROM UserCredentialTable WHERE username = '{username}') ; """)
    
    if cur.fetchone()[0] == True:
        cur.execute(f""" SELECT password FROM UserCredentialTable WHERE username = '{username}' ; """)
        secretPassword = password.encode("utf-8")
        secretPassword = hashlib.sha256(secretPassword).hexdigest()
        
        storedHash = cur.fetchone()[0]
        #print(secretPassword ,storedHash)
        
        if secretPassword == storedHash :
            cur.execute(f""" SELECT id FROM UserCredentialTable WHERE username = '{username}' ; """)
            id = cur.fetchone()[0]
            AppendSessionToken(username,cur,id)
            conn.commit()
            cur.close()
            conn.close()
            return {"Vaild":True ,"ClientPasswordHash":secretPassword,"StoredPasswordHash":storedHash, "ERROR":"NONE","Username":username}
        
        elif secretPassword != storedHash:
            conn.commit()
            cur.close()
            conn.close()
            return {"Vaild":False ,"ClientPasswordHash":secretPassword,"StoredPasswordHash":storedHash , "ERROR": "PASSWORD DOESNT MATCH"}
    else:
        conn.commit()
        cur.close()
        conn.close()
        return {"Vaild":False,"ERROR":"RECORD DOESNT EXIST"}
    

    
@router.post("/SignUp")
async def signUp(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="postgres",
    port=5432
    )

    cur = conn.cursor()
    print(password,username)
    CHECK = signUpValidate(username,password)
    if CHECK == True:
        secretPassword = password.encode("utf-8")

        cur.execute(f""" SELECT EXISTS (SELECT password FROM UserCredentialTable WHERE username = '{username}') ; """)
        if cur.fetchone()[0] == False:
            cur.execute(f""" INSERT INTO UserCredentialTable(Username, password) VALUES ('{username}','{hashlib.sha256(secretPassword).hexdigest()}') ; """)
            conn.commit()
            cur.close()
            conn.close()
            return {"Valid":True}
        else:
            conn.commit()
            cur.close()
            conn.close()
            return {"Valid":False,"ERROR": "USERNAME IN DATABASE"}

        
        
    else:
         return {"Valid":False,"ERROR": "NOT UP TO SPEC"}

@router.post("/SignOut")
async def signOut(id: AuthIDcheck):


    conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="postgres",
    port=5432
    )
    cur = conn.cursor()
    try:


        cur.execute(f"""UPDATE usercredentialtable SET infostatus = 'False' WHERE username =  $${id.id}$$;""")

        conn.commit()
        cur.close()
        conn.close()

        return {"info":"done"}
    except:
        conn.commit()
        cur.close()
        conn.close()
        return {"info":"notDone"}



    
    