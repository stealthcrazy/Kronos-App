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




def signUpValidate(username: str , password: str):
    SPECIAL_CHRS = ["!","@","$","&","*","#"]
    NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]
    UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    USERNAME_CHECK = username.isalnum() & (len(username)<256)
    f1 = False
    f2 = False
    f3 = False
    f4 = False
    for i in password:
        if i in SPECIAL_CHRS:
            f1 = True
            break
    for i in password:
        if i in NUMBERS:
            f2 = True
            break
    for i in password:
        if i in UPPER:
            f3 = True
            break
    for i in password:
        if i in LOWER:
            f4 = True
            break
    print(f1,f2,f3,f4 ,password.isascii(),(len(password)>=8) )
    PASSWORD_CHECK = password.isascii() & (len(password)>=8) & f1 &f2 &f3 &f4
    return PASSWORD_CHECK & USERNAME_CHECK