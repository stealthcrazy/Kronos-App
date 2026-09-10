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





class TextPrompt(BaseModel):
    username: str
    chatInfo: str
    MessageId: str
    prompt: str
class AuthIDcheck(BaseModel):
    id: str
class chatReq(BaseModel):
    username: str
    chatname: str

class TextMarkovFormat(BaseModel):
    Text: str
