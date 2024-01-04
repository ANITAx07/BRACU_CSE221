import math
import heapq
with open('E:\CSE221\A-6\TASK-2\input1.txt','r') as abc:
    f=open('E:\CSE221\A-6\TASK-2\output.txt','w')
    var=abc.readline().split(' ')
    # print(var)
    vertices=int(var[0])
    edge=int(var[1])
    adj_lst=[]  
    for j in range(vertices+1):
        adj_lst.append([])
    for i in range(edge):
        x,y,z=[int(i) for i in abc.readline().split(' ')]
        adj_lst[x].append([y,z])
      
    s=abc.readline().split(' ')
    s1=int(s[0])
    s2=int(s[1])
   
    visited=[0]*(vertices+1)
    parent=[0]*(vertices+1)
    distance_s1=[math.inf]*(vertices+1)
    distance_s2=[math.inf]*(vertices+1)
    prioQ=[]
    distance_s1[s1]=0
    distance_s2[s2]=0
  
    def dijkstra(G,s,distance):
        # distance[s]=0
        visited[s]=1
        prioQ.append(s)
        while prioQ:
            u=heapq.heappop(prioQ)
            # print(u)
            for i in G[u]:
                e=i[0]
                w=i[1]
                if visited[e]==0:
                    visited[e]=1
                
                if distance[u] + w < distance[e]:
                    distance[e]=distance[u] + w
                    heapq.heappush(prioQ,e)
          
        return distance
      
d1 = dijkstra(adj_lst,s1,distance_s1) 
d2 = dijkstra(adj_lst,s2,distance_s2) 

# print(d1.count(math.inf))       
if len(d1)-1 == d1.count(math.inf) or len(d2)-1 == d2.count(math.inf):
    f.write('Impossible')       
else:
    for i in range(1,vertices+1):
        if d1[i] == math.inf:
            d1[i] = -1
        if d2[i] == math.inf:
            d2[i] = -1
         
    v2=[0]*(vertices+1)
    print(d1) 
    print(d2) 
    for i in range(1,vertices+1):
        if d1[i]!=-1 and d2[i]!=-1:
            a=max(d1[i],d2[i])
            v2[i]=a
    d1=d1[1:]
    d2=d2[1:]  
    # print(v2)      
    v=sorted(v2) 
    # print(v)
    for i in range(len(v)):
        if v[i]!=0:
            f.write(f'Time:{v[i]}\nNode:{v2.index(v[i])}') 
            break      
               
