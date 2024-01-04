class Node:
    def __init__(self,elem,next):
        self.elem = elem 
        self.next = next 

class Queue:
    def __init__(self):
        self.front = None
        self.back = None 
    
    def enqueue(self,elem):
        if self.front is None:
            self.front = Node(elem,None)
            self.back = self.front 
        else:
            newNode = Node(elem,None)
            self.back.next = newNode 
            self.back = newNode 
    
    def dequeue(self):
        if self.front is not None:
            x = self.front 
            self.front = self.front.next 
            return x.elem  
        else:
            print("Empty Queue")
    
    def isEmpty(self):
        if self.front is None :
            return True 
        return False 
    
    def printQueue(self):
        p = self.front
        while p is None:
            print(p.elem,end=' ')
            p = p.next

with open('E:\A4\TASK-2\input2_4.txt', 'r') as abc:
    f=open('E:\A4\TASK-2\output.txt', 'w')
    var=abc.readline().split("\n")
    m=var[0].split(' ')
    vertices=int(m[0])
    edges=int(m[1])
    q = Queue()
    adj_list = []
    
    for i in range(vertices+1):
        adj_list.append([])
   
    for i in range(edges):
        s,d = abc.readline().split(' ')
        s = int(s)
        d =int(d)
        adj_list[s].append(d)
        adj_list[d].append(s)  
    color=[0]*(vertices+1)
    
    def BFS(G,s):
        color[s]=1
        q.enqueue(s)
        while not q.isEmpty():
            u=q.dequeue()
            f.write(f'{u}{' '}')
            for i in G[u]:
                if color[i]== 0:
                    color[i]=1
                    q.enqueue(i)
    BFS(adj_list,1)
    
    

