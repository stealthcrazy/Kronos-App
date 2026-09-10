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

import datetime




async def updateUserChatMessages(prompt,response,username,chatInfo,MessageIDS:tuple):
    conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="postgres",
    port=5432
    )
    cur = conn.cursor()
    try:
        cur.execute(f""" SELECT EXISTS (SELECT chatname FROM chattable WHERE username = '{username}' AND chatname = $${chatInfo}$$) ; """)
        CHECK = cur.fetchone()[0]
    except:
        CHECK = False
        pass
    print(chatInfo,CHECK)
    # ran into problem that chatnames have to be unique , no user can take another chatname
    # i now removed constraints from table and reworking to add chatID to chattable that will act as a unqiue primary key
    if (chatInfo!="Default") and (CHECK !=False) :


        cur.execute(f""" INSERT INTO Messages(chatname, messageid,promptid,prompt,response,username) VALUES ($${chatInfo}$$,$${MessageIDS[0]}$$,$${MessageIDS[1]}$$,$${prompt}$$,$${response}$$,$${username}$$) ; """)
    else:
        cur.execute(f""" INSERT INTO chattable(username,chatname) VALUES ('{username}',$${prompt[:20]}$$ )""")
        cur.execute(f""" INSERT INTO Messages(chatname, messageid,promptid,prompt,response,username) VALUES ($${prompt[:20]}$$,$${MessageIDS[0]}$$,$${MessageIDS[1]}$$,$${prompt}$$,$${response}$$,$${username}$$) ; """)
    conn.commit()
    cur.close()        
    conn.close()

async def GetMemory(c):
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
                                SELECT Messages.Prompt , Messages.Response
                                FROM UserCredentialTable
                                INNER JOIN Chattable ON UserCredentialTable.username = Chattable.username
                                INNER JOIN Messages ON Chattable.chatname = Messages.Chatname
                                WHERE Chattable.chatname = $${c}$$;
                                """)
        X = cur.fetchall()
        Memory = ""

        for i in X:
            Memory+= f"</s>Person: {i[0]} ChatBot: {i[1]} </s>"
        print(Memory)
    except:
        print("hmm")
        Memory = ""

    return Memory