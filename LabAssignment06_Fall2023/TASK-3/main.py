with open('E:\CSE221\A-6\TASK-3\input1.txt','r') as abc:
    f=open('E:\CSE221\A-6\TASK-3\output.txt','w')
    var=abc.readline().split(' ')

    vertices=int(var[0]) #5
    edge=int(var[1])    #3
    
    parent=[]
    for i in range(vertices):
        parent.append(i)
    rank=[1]*(vertices+1)
   
    def find_path(a):
        if parent[a] == a:
            return a
        return find_path(parent[a])
    
    def union(a, b):
        u = find_path(a)
        v = find_path(b)
        if u != v:
            parent[u] = v
            rank[v] += rank[u]
        f.write(f'{rank[v]} \n')

    for i in range(edge):
        a, b = [int(i) for i in abc.readline().split(' ')] 
        union(a,b)  

