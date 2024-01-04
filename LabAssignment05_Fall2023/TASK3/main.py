class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next

class Stack:
  def __init__(self):
    self.__top = None

  def push(self,elem):
    if self.__top == None:
      self.__top = Node(elem,None)
    else:
      newN = Node(elem,None)
      newN.next = self.__top
      self.__top = newN

  def pop(self):
    if self.__top == None:
      return None
    else:
      p = self.__top
      self.__top = self.__top.next
      p.next = None
      return p.elem

  def peek(self):
    if self.__top == None:
      return None
    else:
      return self.__top.elem

  def isEmpty(self):
    if self.__top == None:
       return True
    else:
      return False

with open('E:\CSE221\Assignment - 5\TASK3\input2.txt','r') as abc:
    f=open('E:\CSE221\Assignment - 5\TASK3\output.txt','w')
    var=abc.readline().strip().split(' ')
    # print(var)
    vertices=int(var[0])  
    edge=int(var[1])  
    visited1=[0]*(vertices+1) 
    visited2=[0]*(vertices+1) 
    adj_list=[]
    transpose=[]
    stck=Stack()
    scc=[]
    # print(visited1)
    for i in range(vertices+1):
          adj_list.append([])
   
    for i in range(vertices+1):
          transpose.append([])

    for i in range(edge):
        s,d = abc.readline().strip().split(' ')
        s = int(s) 
        d = int(d) 
        adj_list[s].append(d)  
        transpose[d].append(s)  
      
    
    def DFS(G,s): 
        if visited1[s] == 0:   
            visited1[s] = 1
            for i in G[s]:        
                if visited1[i] == 0:  
                    DFS(G, i)           
        stck.push(s)  

    def DFS_in_transposeGraph(transpose_G, s, lst1):
       if visited2[s] == 0:
            visited2[s] = 1
            lst1.append(s)
            for i in transpose_G[s]: 
                if visited2[i] == 0:
                    DFS_in_transposeGraph(transpose, i,lst1) 
       
DFS(adj_list,1)
for i in range(1,len(visited1)):
    if visited1[i] != 1:
        DFS(adj_list,i)

while not stck.isEmpty():
   u=stck.pop()
   if visited2[u] == 0:
      lst1=[]
      DFS_in_transposeGraph(transpose,u,lst1)         
      scc.append(lst1)
      scc.sort()
# print(scc)

for j in scc:
   f.write(" ".join(map(str, j)))
   f.write('\n')      
