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

with open('E:\CSE221\Assignment - 5\TASK1\A\input3.txt','r') as abc:
    f=open('E:\CSE221\Assignment - 5\TASK1\A\output.txt','w')
    var=abc.readline().strip().split(' ')
    # print(var)
    vertices=int(var[0])
    edge=int(var[1])
    visited=[0]*(vertices+1)
    colour = [-1] * (vertices + 1)
    adj_list=[]
    stck=Stack()
    
    for i in range(vertices+1):
          adj_list.append([])

    for i in range(edge):
      s,d = abc.readline().split(' ')
      s = int(s)
      d = int(d)
      adj_list[s].append(d)
    
    xyz=[] 
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
    
    def DFS(G,s):
        if visited[s] == 0:
           visited[s] = 1
           for i in G[s]: 
                if visited[i] == 0:
                    DFS(G, i)
        if s not in xyz:       
            xyz.append(s)  
            stck.push(s)

for i in range(1,len(visited)):
   if colour[i] == -1:
      cycle=check_cycle(adj_list,i)
      if cycle == True:
         cyclic=True
         break
         
if cyclic:
    f.write("Impossible")
else:
    DFS(adj_list,1)
    for i in range(1,len(visited)):
        if visited[i] != 1:
            DFS(adj_list,i)
    
    for i in range(vertices):
        f.write(f'{stck.pop()} ')