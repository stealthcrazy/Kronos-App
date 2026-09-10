


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

PQ = PriorityQueue([
    PriorityQueue.Node("bob",5),
    PriorityQueue.Node("rob",10),
    PriorityQueue.Node("cob",3),
    PriorityQueue.Node("mob",2),
    PriorityQueue.Node("tob",19),

])


PQ.MaxHeapInsert(PriorityQueue.Node("sob",100))

print(PQ.MaxHeapExtractMax().key)





