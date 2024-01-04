with open('E:\A4\TASK-3\input3_4.txt', 'r') as abc:
    f=open('E:\A4\TASK-3\output.txt', 'w')
    var=abc.readline().strip().split(" ")
    vertices=int(var[0])
    edges=int(var[1])
    visited=[0]*(vertices+1)
    adj_lst=[]
    
    for i in range(vertices+1):
        adj_lst.append([])
    
    for i in range(edges):
        u,v=abc.readline().strip().split(' ')
        u=int(u)
        v=int(v)
        adj_lst[u].append(v)
        adj_lst[v].append(u)
    
    def DFS(G, s):
        if visited[s] == 0:
            f.write(f'{s} ')
            visited[s] = 1
            for i in range(len(G[s])):
                if G[s][i] != None and visited[G[s][i]] == 0:
                    DFS(G , G[s][i])  
DFS(adj_lst, 1)   