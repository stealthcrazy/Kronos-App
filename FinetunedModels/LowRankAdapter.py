import torch
import torch.nn as nn

class LoRA(nn.Module):


    def __init__(self,K,rank,alpha):
        super(LoRA,self).__init__()

        self.D_in = K.in_features
        self.D_out = K.out_features
        self.rank  = rank
        self.alpha = alpha
        self.K= K 

        self.K_forward = K.forward
        K.forward = self.forward

        K.A = nn.Parameter(torch.empty(self.D_in,rank).normal_(0,std=0.02))
        K.B = nn.Parameter(torch.zeros(rank,self.D_out))


        

    def forward(self,X):

        return self.K_forward(X) +  ((self.alpha/self.rank)*(X@self.K.A@self.K.B))
    
