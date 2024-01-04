import numpy as np
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

with open('E:\A4\TASK-5\input5_1.txt', 'r') as abc:
    f=open('E:\A4\TASK-5\output.txt', 'w')
    var=abc.readline().split(" ")
    vertices=int(var[0])
    edges=int(var[1])
    destination = int(var[2])
    q = Queue()
    matrix = np.zeros((vertices+1,vertices+1),dtype=int)
    print(matrix)
    for i in range(edges):
        r,c = abc.readline().split(' ')
        r = int(r)
        c =int(c)
        matrix[r][c] = 1
        matrix[c][r] = 1
    visited = [0]*(vertices+1)
    parent = [0]*(vertices+1)
    distance = [0]*(vertices+1)

    def BFS(firs_vrtx):
        visited[firs_vrtx] = 1 
        distance[firs_vrtx] = 0
        q.enqueue(firs_vrtx)

        while not q.isEmpty():
            u = q.dequeue()
            for v in range(1,vertices+1):         
                if matrix[u][v] ==1 and visited[v] == 0:
                    visited[v] = 1 
                    parent[v] = u
                    distance[v] = distance[u]+1     
                    q.enqueue(v)
    BFS(1)
    f.write(f"Time: {distance[destination]}\n")
    path = []
    while destination!=0:
        path.append(destination)
        destination = parent[destination]

    path =path[::-1]
    f.write("Shortest Path: ")
    for i in path:
        f.write(f"{i} ")
    

    
