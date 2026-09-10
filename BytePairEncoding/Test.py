from transformers import GPT2Tokenizer
import json


tokenizer = GPT2Tokenizer.from_pretrained("facebook/opt-125m")


X = [tokenizer.decode(i) for i in range(50265)]


with open("Jalapeno.json","w") as f:
    json.dump(X,f)

