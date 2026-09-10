import torch
import torch.nn as nn
from Backend.TransformerModel import Transformer
import LowRankAdapter
import tiktoken
import os
import random
import time

from transformers import GPT2Tokenizer

#enc = tiktoken.get_encoding("gpt2")
#tokenizer = GPT2Tokenizer.from_pretrained("facebook/opt-2.7b")
tokenizer = GPT2Tokenizer.from_pretrained("facebook/opt-125m")

"""
ModelDimension = 2560
Heads = 32
ForwardExpansion = 4
Layers = 32
VOCABLEN = 50272 
#VOCABLEN = enc.n_vocab
MAXLEN = 2048
"""
ModelDimension = 768
Heads = 12
ForwardExpansion = 4
Layers = 12
VOCABLEN = 50272 
#VOCABLEN = enc.n_vocab
MAXLEN = 2048



device = torch.device("cpu")

model = Transformer( ModelDimension, Heads, ForwardExpansion, Layers, VOCABLEN, MAXLEN,device=device,DRP=0.0)
#torch.save(model.state_dict(),"111BB")
#exit()
RequiresAdapter = ["Attention.Q","Attention.V",]
Rank = 8
alpha = 16
    

for name,module in model.named_modules():
    for j in RequiresAdapter:
        if j in name:
            a = LowRankAdapter.LoRA(module,Rank,alpha)
#checkpoint = torch.load("LEMON_MakesSense.pth" , map_location=torch.device("cpu"),weights_only=False)
checkpoint = torch.load("cITRIC.pth" , map_location=torch.device("cpu"),weights_only=False)
model.load_state_dict(checkpoint["Model"],strict=True)
#model.load_state_dict(checkpoint,strict=True)



prompt ="""</s>Person: Hello Chatbot: """
#prompt ="""Person: Is the eifel tower in france </s>Chatbot: """

#Token = torch.tensor([enc.encode("""Once upon a time """)])
Token = tokenizer([prompt], return_tensors="pt")["input_ids"]

Token = torch.tensor([list(Token[0])])

m = Token.shape[1]-1
print(m)

NOTB=True

for _ in range(1024) :
    model.eval()
    print(f"current Token: {_}")
    print([tokenizer.decode(i) for i in Token][0])
    #print(enc.decode(list(Token[0])))
    
    o = model(Token)
    print(o.shape)
    #print(o)
    o = nn.functional.softmax(o[0])
    #print(o)
    #time.sleep(1)
    
    
    #print(random.choice(torch.topk(o[0][_] , 10,).indices))
    prob , indi =  torch.topk(o[m+_],50,)
    
    
    
    
    
    #normK =nn.functional.softmax(prob,dim=-1)
    #dist=torch.distributions.categorical.Categorical(probs=normK)
    #m = dist.sample()
    dist = torch.multinomial(prob,1)
    
    s = torch.tensor([indi[dist[0]]])
    
    
    """
    Prob = o[0][_] / temp
    Prob = torch.nn.functional.softmax(Prob, dim=0)

    dist=torch.distributions.categorical.Categorical(probs=Prob)
   
    m = dist.sample()"""
    
    #Token = torch.cat((Token,torch.tensor([[int(torch.argmax(o[0][_]))]])),1) 
    #Token = torch.cat((Token,torch.tensor([[int(torch.multinomial(o[0][_] , num_samples=1 ,))]])),1) 
    #Token = torch.cat((Token,torch.tensor([[int(Categorical(logits=o[0][_] / 0.1).sample())]])),1) 
    #Token = torch.cat((Token,torch.tensor([[int(random.choice(torch.topk(o[0][_] , 10,).indices))]])),1) 
    #Token = torch.cat((Token,torch.tensor([[int(dist.sample())]])),1) 
    
    Token = torch.cat((Token,torch.tensor([[int(s)]])),1)
    
    os.system("clear")
    if int(s)==2:
        break
    #print(enc.decode(list(Token[0])))
    
#print(Token)
print(Token)
print([tokenizer.decode(i) for i in Token][0])
#print(enc.decode(list(Token[0])))
print("---------------------------------------------------------------------------")
