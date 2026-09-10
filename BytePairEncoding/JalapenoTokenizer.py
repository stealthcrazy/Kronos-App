

import time
import json




class Jalapeno:
     
    def __init__(self):
        with open("BytePairEncoding/Jalapeno.json") as f:
            self.vocab = json.load(f)
            self.VOCAB = {}
            c = 0

            for i in self.vocab:
                self.VOCAB[i] = c
                c+=1
    @staticmethod
    def ENCODE(txt,vocab):

        
        d = []
        lenV = len(txt)
        
        _ = 0
        while _ < lenV:
                if _!=lenV-1 and txt[_]+txt[_+1] in vocab:
                        d.append(txt[_]+txt[_+1])
                        _+=2
                        
                else:
                    d.append(txt[_])
                        #d.append(v[_+1])
                    _+=1
        
        if txt != d:
            d = Jalapeno.ENCODE(d , vocab)
        return d
    def encode(self,s):
        return [self.VOCAB[i] for i in Jalapeno.ENCODE(s,self.vocab)]
         
    def decode(self,X):
        S = ""
        for i in X:
            S+=self.vocab[i]
        return S
        





#print(s)


