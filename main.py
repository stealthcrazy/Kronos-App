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

from Backend import AuthenticationMethods , ChatMethods , FormMethods ,  Model ,MarkovChains

#enc = tiktoken.get_encoding("gpt2")




app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(AuthenticationMethods.router)
app.include_router(ChatMethods.router)
app.include_router(FormMethods.router)
app.include_router(Model.router)
app.include_router(MarkovChains.router)

    




