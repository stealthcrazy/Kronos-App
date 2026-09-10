
import time


class Heap:
    def __init__(self, A,N) -> None:
        self.HeapSize = N-1
        self.BuildMaxHeap(A)
        self.Heap =A

    def Parent(i):
        i+=1
        return (i//2)-1
    def Left(i):
        i+=1
        return (2*i)-1
    def Right(i):
        i+=1
        return ((2*i)+1)-1
    
    def MaxHeapify(self,A,i):
    #print(A)
        l = Heap.Left(i)
        r = Heap.Right(i)

        if l<= self.HeapSize and A[l].key>A[i].key:
            largest = l
        else:
            largest = i
        if r<= self.HeapSize and A[r].key > A[largest].key : 
            largest = r
        if largest != i:
            temp = A[i]
            A[i]=A[largest]
            A[largest]= temp
            self.MaxHeapify(A,largest)
    def BuildMaxHeap(self,A):
        for i in range(self.HeapSize,-1 , -1):
            #print(i)
            self.MaxHeapify(A,i)
    



class PriorityQueue:
    class Node:
        def __init__(self,x,key) :
            self.value = x
            self.key = key


    def __init__(self,A):
        self.H = Heap(A,len(A))
        self.Heap = self.H.Heap
    

    def MaxHeapIncreaseKey(self,x,k):
        
        assert not k < x.key , "new key is smaller than current key"
        
        x.key = k
        i = self.Heap.index(x)
        while i > 0 and self.Heap[Heap.Parent(i)].key < self.Heap[i].key : 
                temp = self.Heap[i]
                self.Heap[i] = self.Heap[Heap.Parent(i)]
                self.Heap[Heap.Parent(i)] = temp
                i = Heap.Parent(i)
    def MaxHeapInsert(self ,x):
        
        self.H.HeapSize +=1 
        
        k = x.key
        x.key = -1e20
        self.Heap.append(x)
        self.MaxHeapIncreaseKey(x,k)
    def MaxHeapMaximum(self):
        
        assert not self.H.HeapSize <0, "heap underflow"
        return self.Heap[0]
    def MaxHeapExtractMax(self):
        
        max = self.MaxHeapMaximum()

        self.Heap[0] = self.Heap[self.H.HeapSize]
        self.H.HeapSize-=1
        self.H.MaxHeapify(self.Heap,0)
        return max









with open("test.txt" , "r") as f:
    s = f.read()
    vocab = [i for i in list(set(s))]
    data = s.split()


        
def Pair(A,C,k):
    
    
    #print(A)
    for i in range(len(A)-1):
        
        if (A[i]+A[i+1]) not in C:
           #if A[i] =="ou":
               #print(A[i]+A[i+1])
           C[(A[i]+A[i+1])] =k
        else:
            C[(A[i]+A[i+1])] +=k
    
    


def Merge(C,vocab):
    vocab  = set(vocab)
    D = {}
    
    for v,k in C.items():
        d=[]
        #print(v)
      
        _ = 0
        #print(v)
        lenV = len(v)
        while _ < lenV:
                
                if _!=lenV-1 and v[_]+v[_+1] in vocab:
                        d.append(v[_]+v[_+1])
                        _+=2
                    
                else:
                        d.append(v[_])
                        #d.append(v[_+1])
                        _+=1

            
            
            

        #print(d)
        D[tuple(d)] = k
    return D
"""
def Extract(C,D):
    for v,k in C.items():
        #print(v)
        M = Pair(v)
        for V,K in M.items():
                
            if V not in D:
                D[V] = K*k 
            else:
                D[V] += K*k """
def Extract(C):
    D = {}
    for v,k in C.items():
        Pair(v,D,k)
    #print(D)
    return D

        

def Encode(data,vocab,MaxTokens):
    C = {}
    for i in data:
        if i not in C:
            C[i] =1
        else:
            C[i]+=1
    #print(C)
    #print(len(C))
    
   
    
    
    D = Extract(C)
    #print(D)
    
    PQ = PriorityQueue([
                PriorityQueue.Node(Value , Key) for Value ,Key in D.items()
            ])
    X = set(i.value for i in PQ.Heap)
    #print(PQ.H.HeapSize)

    for ___ in range(MaxTokens):
        S = time.time()
        print(___ , end = " ")
        #print(PQ.H.HeapSize)
        #print(C)
        #print([i.value for i in PQ.Heap])
        
        
        
        
        MK= PQ.MaxHeapExtractMax()
        #print(MK.value , MK.key)
        
        
        vocab.append(MK.value)
        C = Merge(C,vocab)
        #print(time.time()-S,end = " ")
        
        M = time.time()
        D = Extract(C)
        #print(time.time()-M,end = " ")
        
        #print(D)
        
        for v,k in D.items():
            
            if v not in X:
                M = PriorityQueue.Node(v,k)
                PQ.MaxHeapInsert(M)
                X.add(v)
        E = time.time()
        print(E-S)
        #print(vocab)
    return data
#print(len(data))
start = time.time()
Encode(data,vocab,1000)
end = time.time()
print(vocab)
print(end-start)