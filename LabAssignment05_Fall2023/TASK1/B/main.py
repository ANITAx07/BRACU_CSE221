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

with open('E:\CSE221\Assignment - 5\TASK1\B\input1.txt','r') as abc:
    f=open('E:\CSE221\Assignment - 5\TASK1\B\output.txt','w')
    var=abc.readline().strip().split(' ')
    vertices=int(var[0])
    edge=int(var[1])
    visited=[0]*(vertices+1)
    colour = [-1] * (vertices + 1)
    adj_list=[]
    q=Queue()
   
    for i in range(vertices+1):
        adj_list.append([])

    for i in range(edge):
        u,v=abc.readline().strip().split(' ')
        u=int(u)
        v=int(v)
        adj_list[u].append(v)
        visited[v] += 1
          
    lst=[] 
    cyclic = False
    def check_cycle(G, u):
        global cyclic
        if colour[u] == -1:
            colour[u] = 0
            for v in G[u]:
                if colour[v] == -1:
                    check_cycle(G,v)
                elif colour[v] == 0:
                    cyclic = True
            colour[u] = 1
        return cyclic
    
    def BFS(G):
        for i in range(1,vertices+1): 
            if visited[i] == 0:
              q.enqueue(i)
        
        while not q.isEmpty():
            u=q.dequeue()
            if u not in lst:
              lst.append(u)
            for j in G[u]:
                visited[j] -= 1
                if visited[j] == 0:
                    q.enqueue(j)


for i in range(1,len(visited)):
   if colour[i] == -1:
      cycle=check_cycle(adj_list,i)
      if cycle==True:
         cyclic=True
         break                   
                        
if cyclic:
    f.write("Impossible")
else:
    BFS(adj_list)
    for i in range(1,len(visited)):
        if visited[i] != 1:
            BFS(adj_list)
    
    for i in lst:
        f.write(f'{i} ')

