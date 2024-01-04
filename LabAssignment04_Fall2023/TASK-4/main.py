with open('E:\A4\TASK-4\input4_1.txt', 'r') as abc:
    f=open('E:\A4\TASK-4\output.txt', 'w')
    var=abc.readline().split(" ")
    vertices=int(var[0])
    edges=int(var[1])
    adj_list = []
    
    for i in range(vertices+1):
        adj_list.append([])
   
    for i in range(edges):
        s,d = abc.readline().split(' ')
        s = int(s)
        d =int(d)
        adj_list[s].append(d)
        colour = [-1] * (vertices + 1)
        cyclic = False

    def DFS(G, u):
        global cyclic
        if colour[u] == -1:
            colour[u] = 0
            for v in G[u]:
                if colour[v] == -1:
                    DFS(G,v)
                elif colour[v] == 0:
                    cyclic = True
            colour[u] = 1

DFS(adj_list,1)      
if cyclic:
    f.write("YES")
else:
    f.write("NO")


