import math
import heapq
with open('E:\CSE221\A-6\TASK-1\input2.txt','r') as abc:
    f=open('E:\CSE221\A-6\TASK-1\output.txt','w')
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

    
    source=int(abc.readline()) #1
    visited=[0]*(vertices+1) 
    distance=[math.inf]*(vertices) 
    prioQ=[]
    
    for i in range(1,vertices+1):
        prioQ.append(i)
    heapq.heapify(prioQ)
    
    def dijkstra(G,s):
        distance[s-1]=0  
        visited[s]=1     
    
        while prioQ:
            u=heapq.heappop(prioQ)  

            for i in G[u]:  #[3, 2]
                e=i[0] #3
                w=i[1] #2
                if visited[e] == 0: #e=3
                    visited[e] = 1  
                
                if distance[u-1] + w < distance[e-1]:
                    distance[e-1]=distance[u-1] + w     
                    heapq.heappush(prioQ,e) 
                 
        return distance
       
dijkstra(adj_lst,source)
print(distance)

for i in distance:
    if i == math.inf:
        f.write (f'{-1} ')  
    else:
        f.write(f'{i} ') 
