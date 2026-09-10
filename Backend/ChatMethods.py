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






from Backend.DataFormats import *


from fastapi import APIRouter



router = APIRouter(
    prefix="/ChatMethods",
    tags=["ChatMethods"],
)


@router.post("/DeleteChats")
async def DeleteChats(data: chatReq):
    conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="postgres",
    port=5432
    )
    cur = conn.cursor()
    print("hi")
    try:
       cur.execute(f""" DELETE FROM chattable WHERE username =$${data.username}$$ AND chatname = $${data.chatname}$$;""")
       cur.execute(f""" DELETE FROM messages WHERE username =$${data.username}$$ AND chatname = $${data.chatname}$$;""")
       
       
       
       
       
       
       conn.commit()
       
       cur.close()
       conn.close()
       
       print("done")
       
       return {"status":"done"}
        


    except ValueError:
        print("error")
        return {"status":"None"}
    
@router.post("/ChatMessages")
async def getChatMessages(data: chatReq):
    conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="postgres",
    port=5432
    )
    cur = conn.cursor()
    try:
        if data.chatname != "Default":
            cur.execute(f"""
                        SELECT UserCredentialTable.username, Messages.Prompt , Messages.Response
                        FROM UserCredentialTable
                        INNER JOIN Chattable ON UserCredentialTable.username = Chattable.username
                        INNER JOIN Messages ON Chattable.chatname = Messages.Chatname
                        WHERE Chattable.chatname = $${data.chatname}$$ AND UserCredentialTable.username = $${data.username}$$ ;
                        """)
            X = cur.fetchall()
            print(X, "     --")
            Messages = []
            for i in  range(len(X)):
                Messages.append(X[i][1])
                Messages.append(X[i][2])
            print(Messages)
            return {'MessageInfo':Messages , "Void":False}
        else:
            return {"MessageInfo":"None"}
        


    except:
        return {"MessageInfo":"None"}
    
@router.post("/ChatNames")
async def getChatMessages(data: chatReq):
    conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="postgres",
    port=5432
    )
    cur = conn.cursor()
    try:
        cur.execute(f"""
                        SELECT UserCredentialTable.username, Chattable.Chatname
                        FROM UserCredentialTable
                        INNER JOIN Chattable ON UserCredentialTable.username = Chattable.username
                        WHERE UserCredentialTable.username = $${data.username}$$;
                        
                        """)
        X = cur.fetchall()
        print(X)
        Chats = []
        for i in  range(len(X)):
            Chats.append(X[i][1])
        print(Chats)
        return {'MessageInfo':"None" , "Void":True ,"ChatInfo":Chats}
            

            


    except IndentationError:
        return {"MessageInfo":"None"}
    
