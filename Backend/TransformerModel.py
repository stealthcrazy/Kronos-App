import torch
import torch.nn as nn


class Transformer(nn.Module):
    

    def __init__(self, ModelDimension, Heads, ForwardExpansion, Layers, VOCABLEN, MAXLEN, device, DRP):
        super(Transformer,self).__init__()

        self.ModelDimension = ModelDimension
        self.Heads = Heads
        self.ForwardExpansion = ForwardExpansion
        self.Layers = Layers
        self.VOCABLEN = VOCABLEN
        self.MAXLEN = MAXLEN

        self.device = device
        self.DRP = DRP
        self.Dropout = nn.Dropout(DRP)

        self.WordEmbedding = nn.Embedding(self.VOCABLEN , self.ModelDimension , device=self.device)
        self.PositionalEmbedding = nn.Embedding(self.MAXLEN +2, self.ModelDimension,device=self.device)

        

        self.NORM3 = nn.LayerNorm(self.ModelDimension)
        self.DECODER_ =DECODER(self.ModelDimension, self.Heads, self.ForwardExpansion, self.Layers, self.VOCABLEN, self.MAXLEN, self.DRP)

        
        self.OUT = nn.Linear(self.ModelDimension, self.VOCABLEN,)
        
        

        self.WordEmbedding.weight = self.OUT.weight
    """
        self.apply(self._init_weights)

    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            std = 0.02
            if hasattr(module, 'CABRON'):
                
                std *= (2 * self.Layers) ** -0.5
            torch.nn.init.normal_(module.weight, mean=0.0, std=std)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
    """
     
    def forward(self, X):
        N = X.shape[0]
        Len = X.shape[1]

        POS = torch.arange(0,Len,device=self.device)

        X =self.Dropout(self.WordEmbedding(X)+ self.PositionalEmbedding(POS))

        X = self.DECODER_(X)
        X = self.NORM3(X)
        X = self.OUT(X)
        
        return X


class DECODER(nn.Module):

    def __init__(self, ModelDimension, Heads, ForwardExpansion, Layers, VOCABLEN, MAXLEN, DRP):
        super(DECODER,self).__init__()
        self.ModelDimension = ModelDimension
        self.Heads = Heads
        self.ForwardExpansion = ForwardExpansion
        self.layers = Layers
        self.VOCABLEN = VOCABLEN
        self.MAXLEN = MAXLEN
        self.DRP = DRP
        


        self.Layers = nn.ModuleList([
            BLOCK(self.ModelDimension, self.Heads, self.ForwardExpansion, self.MAXLEN, self.DRP) for _ in range(self.layers)
        ])
     
    def forward(self,X):
        for layer in self.Layers:
            X = layer(X)
        return X



class BLOCK(nn.Module):
    
    def __init__(self,ModelDimension, Heads, ForwardExpansion, MAXLEN, DRP) -> None:
        super(BLOCK,self).__init__()
        self.ModelDimension = ModelDimension
        self.Heads = Heads
        self.ForwardExpansion = ForwardExpansion
        self.MAXLEN = MAXLEN
        self.DRP =DRP

        self.NORM1 = nn.LayerNorm(self.ModelDimension)
        self.Attention = Attention(self.ModelDimension, self.Heads, self.MAXLEN)
        self.NORM2 = nn.LayerNorm(self.ModelDimension)
        self.FeedForward = FeedForwardLayer(self.ModelDimension, self.ForwardExpansion)
        self.Dropout = nn.Dropout(self.DRP)
        
    def forward(self,X):
        
        X =  self.Dropout(X+self.Attention(self.NORM1(X)))
       
        X =self.Dropout(X+self.FeedForward(self.NORM2(X))) #there was a problem here stupid u put NORM1 INSTEAD NORM2
        
        return X

class FeedForwardLayer(nn.Module):

    def __init__(self,ModelDimension, ForwardExpansion ) -> None:
        super(FeedForwardLayer,self).__init__()
        self.ModelDimension = ModelDimension
        self.ForwardExpansion = ForwardExpansion

        self.L1 = nn.Linear(self.ModelDimension , self.ForwardExpansion *self.ModelDimension)
        #self.GELU = nn.GELU(approximate='tanh')
        self.RELU = nn.ReLU()
        self.L2 = nn.Linear( self.ForwardExpansion *self.ModelDimension, self.ModelDimension)
        #self.L2.CABRON =1
        
     
    def forward(self, X):
        X = self.L1(X)
        #X = self.GELU(X)
        X = self.RELU(X)
        X = self.L2(X)
        return X
    


    
class Attention(nn.Module):

    def __init__(self,ModelDimension, Heads,MAXLEN) -> None:
        super(Attention,self).__init__()
        self.ModelDimension = ModelDimension
        self.Heads = Heads
        self.MAXLEN =MAXLEN

        #self.QKV = nn.Linear(self.ModelDimension, 3*self.ModelDimension)
        self.Q = nn.Linear(self.ModelDimension, self.ModelDimension,bias=False)
        self.K = nn.Linear(self.ModelDimension, self.ModelDimension,bias=False)
        self.V = nn.Linear(self.ModelDimension, self.ModelDimension,bias=False)
        #self.Q = nn.Linear(self.ModelDimension, self.ModelDimension)
        #self.K = nn.Linear(self.ModelDimension, self.ModelDimension)
        #self.V = nn.Linear(self.ModelDimension, self.ModelDimension)

        self.OUT = nn.Linear(self.ModelDimension, self.ModelDimension)
        #self.OUT.CABRON =1

        self.register_buffer("bias", torch.tril(torch.ones(self.MAXLEN,self.MAXLEN)).view(1,1,self.MAXLEN,self.MAXLEN))
     
    def forward(self,X):

        N = X.shape[0]
        Len =X.shape[1]
        C = X.shape[2]

        Q= self.Q(X)
        K = self.K(X)
        V= self.V(X)
        
        Q = Q.reshape(N, Len, self.Heads, C//self.Heads)
        K = K.reshape(N, Len, self.Heads, C//self.Heads)
        V = V.reshape(N, Len, self.Heads, C//self.Heads)
        X = torch.einsum("nqhd,nkhd->nhqk", [Q, K]) /(K.size(-1) ** 0.5)
        X = X.masked_fill(self.bias[:,:,:Len,:Len] == 0, float("-inf"))
        X = torch.nn.functional.softmax(X, dim =-1)
        X = torch.einsum("nhql,nlhd->nqhd", [X, V]).reshape(N, Len, C) 
        X = self.OUT(X)
        """
        q = q.view(N, Len, self.Heads, C // self.Heads).transpose(1, 2)
        k = k.view(N, Len, self.Heads, C // self.Heads).transpose(1, 2) 
        v = v.view(N, Len, self.Heads, C // self.Heads).transpose(1, 2) 


        X = torch.matmul(q, k.transpose(-2,-1)) / (k.size(-1) ** 0.5)
        
        X = X.masked_fill(self.bias[:,:,:Len,:Len]==0 ,float("-inf"))
        X = torch.nn.functional.softmax(X, dim =-1)
        X = torch.matmul(X,v)
        X = X.transpose(1,2).contiguous().view(N,Len,C)
        X = self.OUT(X)
        """
         
        return X

        



        






