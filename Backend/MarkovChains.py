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
import json
import string


from fastapi import APIRouter , Depends

from Backend.DataFormats import TextMarkovFormat
from MarkovChainedChains.MarkovChain import MarkovChains


router = APIRouter(
    prefix="/MarkovChains",
    tags=["MarkovChains"],

)
#v = open("/Users/sohanprabhu/Desktop/Markov Chains K/VocabFree1D.json","r")
#v2 = open("/Users/sohanprabhu/Desktop/Markov Chains K/VocabFree2d.json","r")

@router.post("/ChainedComplete")
async def Response(prompt: TextMarkovFormat):
    print(prompt.Text)

    

    #with open("./temp.txt","w") as f:
        #f.write(prompt.Text)
    
    
    #X = MarkovChains(Ngram=1,fileName="./temp.txt",  )
    G=""
    translator = str.maketrans('', '', string.punctuation)
    d  = prompt.Text
    d= d.translate(translator)
    r = d.split()
    if len(r) >= 5:
        X = MarkovChains(Ngram=1, Text = str(prompt.Text) )
        X.Chains()
        print("X.chained")
        G = X.generate(str(prompt.Text))

    print("D" , G)


    return {"Prediction":G}