with open('E:\CSE221\A-6\TASK-4\input1.txt','r') as abc:
    out=open('E:\CSE221\A-6\TASK-4\output.txt','w')
    var=abc.readline().split(' ')
    vertices=int(var[0])
    edge=int(var[1])
    adj_list=[]
    for i in range(edge):
        f,s,w=abc.readline().strip().split()
        f,s,w=int(f),int(s),int(w)
        adj_list.append((w,f,s))
  
    adj_list.sort()              
    parent=[]
    weight=0
    for i in range(vertices+1):
        parent.append(i)
    
    def path(a):
        if parent[a] == a:
            return a
        return path(parent[a])
    
    def union(a, b,c):
        u = path(a)
        v = path(b)
        if u != v:
            parent[u] = v
            return c
        return 0
    
    for i in adj_list:
        x=union(i[1],i[2],i[0])
        weight += x

min_cost=str(weight)           
out.write(f'{str(min_cost)}')



