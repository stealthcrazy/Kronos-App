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


from BytePairEncoding.JalapenoTokenizer import Jalapeno


from Backend.DataFormats import TextPrompt
from Backend.dependencies import updateUserChatMessages , GetMemory

from FinetunedModels.LowRankAdapter import LoRA

from fastapi import APIRouter , Depends

from contextlib import asynccontextmanager



router = APIRouter(
    prefix="/Model",
    tags=["Model"],

)




#tokenizer = GPT2Tokenizer.from_pretrained("facebook/opt-125m")
tokenizer = Jalapeno()

ModelDimension = 768
Heads = 12
ForwardExpansion = 4
Layers = 12
VOCABLEN = 50272 
#VOCABLEN = enc.n_vocab
MAXLEN = 2048

device = torch.device("cpu")

model = Transformer( ModelDimension, Heads, ForwardExpansion, Layers, VOCABLEN, MAXLEN,device=device,DRP=0.0)


checkpoint = torch.load("./Lemons" , map_location=torch.device("cpu"),weights_only=False)
"""
checkpoint = torch.load("./FinetunedModels/LEMON1.5.pth" , map_location=torch.device("cpu"),weights_only=False)

RequiresAdapter = ["Attention.Q","Attention.V",]
Rank = 8
alpha = 16
    

for name,module in model.named_modules():
    for j in RequiresAdapter:
        if j in name:
            a = LoRA(module,Rank,alpha)"""
model.load_state_dict(checkpoint["Model"],strict=False)


model.eval()






@router.post("/User/{User_ID}/Prompts/{Prompt_ID}")
async def Response(User_ID : int , Prompt_ID  : int , prompt: TextPrompt):


    M = await GetMemory(prompt.chatInfo)

   
    Token = tokenizer.encode(f"{M}</s>Person: {prompt.prompt} ChatBot:" )

    Token = torch.tensor([Token])
    m = Token.shape[1]-1

    notEnd = True
    _ = 0
    while notEnd:
        print(f"current Token: {_}")

        print(tokenizer.decode(list(Token)[0]))

        o = model(Token) 

        o = nn.functional.softmax(o[0],dim=-1)

        prob , indi =  torch.topk(o[m+_],50)

        dist = torch.multinomial(prob,1)

        s = torch.tensor([indi[dist[0]]])

        Token = torch.cat((Token,torch.tensor([[int(s)]])),1)

        _+=1
        print(int(s))
        if (int(s) == 2) or (_>=128):
            notEnd = False
        
    #print(str([tokenizer.decode(i) for i in Token][0])[len(f"{M}</s>"+f"Person: {prompt.prompt} ChatBot):")+3:-1*len("</s>")])
    #print(str([tokenizer.decode(i) for i in Token][0])[len(f"{M}</s>"+f"Person: {prompt.prompt} ChatBot):")+3:-1*len("</s>")])
    print(f"Mids{prompt.MessageId}")
    await updateUserChatMessages(prompt.prompt , str(tokenizer.decode(list(Token)[0]))[len(f"{M}</s>"+f"Person: {prompt.prompt} ChatBot):")+3:-1*len("</s>")], prompt.username , prompt.chatInfo,(prompt.MessageId,prompt.MessageId))
    return {"response" :  str(tokenizer.decode(list(Token)[0]))[len(f"{M}</s>"+f"Person: {prompt.prompt} ChatBot):")+3:-1*len("</s>")],"chatname":prompt.prompt[:20]}

@router.post("/EditMessages")
async def EditPrompt(Data:TextPrompt):
    print(Data)
    conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="postgres",
    port=5432
    )
    cur = conn.cursor()

    M = await GetMemory(Data.chatInfo)
    Token = tokenizer.encode(f"{M}</s>Person: {Data.prompt} ChatBot:" )

    Token = torch.tensor([Token])
    m = Token.shape[1]-1

    notEnd = True
    _ = 0
    while notEnd:
        print(f"current Token: {_}")

        print(tokenizer.decode(list(Token)[0]))

        o = model(Token) 

        o = nn.functional.softmax(o[0],dim=-1)

        prob , indi =  torch.topk(o[m+_],50)

        dist = torch.multinomial(prob,1)

        s = torch.tensor([indi[dist[0]]])

        Token = torch.cat((Token,torch.tensor([[int(s)]])),1)

        _+=1
        print(int(s))
        if (int(s) == 2) or (_>=128):
            notEnd = False
        
    #print(str([tokenizer.decode(i) for i in Token][0])[len(f"{M}</s>"+f"Person: {prompt.prompt} ChatBot):")+3:-1*len("</s>")])
    #print(str([tokenizer.decode(i) for i in Token][0])[len(f"{M}</s>"+f"Person: {prompt.prompt} ChatBot):")+3:-1*len("</s>")])
    print(f"Mids{Data.MessageId}")
    cur.execute(f"""UPDATE messages SET prompt = $${Data.prompt}$$  WHERE chatname = $${Data.chatInfo}$$ AND messageid = $${Data.MessageId}$$ ;""")
    cur.execute(f"""UPDATE messages SET response = $${str(tokenizer.decode(list(Token)[0]))[len(f"{M}</s>"+f"Person: {Data.prompt} ChatBot):")+3:-1*len("</s>")]}$$  WHERE chatname = $${Data.chatInfo}$$ AND messageid =$${Data.MessageId}$$ ;""")
    conn.commit()
    cur.close()        
    conn.close()
    return {"response" :  str(tokenizer.decode(list(Token)[0]))[len(f"{M}</s>"+f"Person: {Data.prompt} ChatBot):")+3:-1*len("</s>")],"chatname":Data.prompt[:20]}
