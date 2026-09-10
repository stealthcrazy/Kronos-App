import random
import time
import numpy as np
import json
import string



class MarkovChains:

    def __init__(self,fileName="small.txt",Ngram=2 , Matrix = None , Vocab1 = [] , Vocab2 = [], Text = None):
        self.Matrix  = Matrix
        
        self.n =Ngram
        if Matrix !=None:
            self.Vocab1 = Vocab1
            self.Vocab2 = Vocab2 
            self.M = np.load(Matrix)

        else:
            self.Vocab1 = [] 
            self.Vocab2 = [] 
            translator = str.maketrans('', '', string.punctuation)
            if Text == None:
                with open(fileName,"r") as f:
                    d = f.read()
                    d= d.translate(translator)

                    #d = d.lower()


                    r = d.split()
            else:

                d = Text
                print(d)
                d= d.translate(translator)
                r = d.split()
            

            for i in r:
                if i not in self.Vocab1:
                    self.Vocab1.append(i)

            G = [ list(r[j+i] for i in range(Ngram)) for j in range(len(r)-Ngram+1)]
            for i in G:
                if i not in self.Vocab2:
                    self.Vocab2.append(i)
            
            

            self.r = r
            self.n =Ngram
            print(self.r , self.Vocab1,self.Vocab2)

            
       
    @staticmethod
    def LaplaceSmoothing(X,alpha):

        L = alpha * np.ones(X.shape)
        return X+L


    def Chains(self,):
        
        V = len(self.Vocab1)

        V2 = len(self.Vocab2)
        T = np.zeros((V2,V))
        
        
        

        for pos in range(len(self.r)-self.n):

            i = self.Vocab2.index(list(self.r[pos+i] for i in range(self.n)))
            j = self.Vocab1.index(self.r[pos+self.n])

            T[i][j]+=1



        X = np.ones((V,1))
                   # row totals
        
        #T = MarkovChains.LaplaceSmoothing(T,1)
        S = T@X  
        #print(S)
        #print(X,T)
        
        

        #NORM PROBABILITY Calc.
        
        #for aa in range(0,V2-1):
            #T[aa] = T[aa]/S[aa]

        
        #Log Probability Calc
        for aa in range(0,V2-1):
            T[aa] = T[aa]/S[aa]
        
        

        self.M = np.log(T)
        #print(self.M, "lop robabs")
        
    @staticmethod
    def sample(D):
        X = []

        D = D.transpose()
        D*=1000


        
        for i in range(len(D)):
                for j in range(int(D[i])):
                    X.append(i)
        if len(X)-1 == -1:

            return None

        c = random.randint(0,(len(X)-1))
        return X[c]

    def generate(self,St):
        l = len(self.Vocab2)
        I = np.zeros((l,1))
        print(self.M)
        #St = St.lower()
        St+=" "
        try:
            G = St.split()
            og = St
            Tk = [G[-i] for i in range(self.n,0,-1)]
            print(Tk)
            #print(self.Vocab2)
            i = self.Vocab2.index(Tk)
            print("h")
            print(Tk ,self.n,1 )
            I[i][0] = 1
            if len(self.Vocab1) >= 5:

                for w in range(1):
                    print(w)


                    SM = None

                    while SM== None:


                        P = I.transpose()@np.exp(self.M)
                        print("in Loops ? ")
                        SM = MarkovChains.sample( P)
                        print("in Loops")
                        if SM == None:
                            I = np.zeros((l,1))
                            I[random.randint(0,l-1)][0] = 1
                            print("Hello there")


                    
                    
                    print(SM)
                    St+=self.Vocab1[SM]+" "
                    G = St.split()
                    I = np.zeros((l,1))

                    Tk = [G[-i] for i in range(self.n,0,-1)]


                    try:
                        i = self.Vocab2.index(Tk)
                        I[i][0] = 1
                    except:
                        I = np.zeros((l,1))
                        I[random.randint(0,len(self.Vocab2)-1)][0] = 1
                    #print(G)
                    


                    
                    
                    
                    if (w+1)%20 == 0:
                        St+="\n"

                
            print(St)
            
            print(St[len(og):] , "___" , St)
            return St[len(og):]
            
        except ValueError:
            print("EE")
            return ""






#print(X.Vocab2,X.Vocab1)


