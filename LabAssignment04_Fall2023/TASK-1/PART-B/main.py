with open('E:\A4\TASK-1\PART-B\input1b_1.txt', 'r') as abc:
   var=abc.readline().split("\n")
   f=open('E:\A4\TASK-1\PART-B\output1b_1.txt', 'w')
   m=var[0].split(' ')
   vertices=int(m[0])
   edges=int(m[1])
   d = {}

   for i in range(vertices+1):
        d.update({i:[]})
        
   for j in range(edges):
        st,end,weight = [int(i) for i in abc.readline().split(' ')]
        d[st].append(str((end,weight)))
    
   for h in range(vertices+1):
        if d[h] == []:
                f.write(f'{h} : \n')
        else:
                f.write(f'{h} : {" ".join(d[h])} \n')