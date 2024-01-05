with open('TASK(3)\INPUT3.txt', 'r') as abc:
    var=abc.readlines()    
    n=int((var[0]))
    id=(var[1].split(' '))
    mark=var[2].split(' ')
    
    for i in range(n):
        id[i]=int(id[i])
      
    for i in range(n):
        mark[i]=int(mark[i])
    
    f=open('TASK(3)\OUTPUT3.txt', 'w')
    
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if mark[min] < mark[j]:
                min = j

            if mark[min] == mark[j]:
                if id[min] > id[j]:
                    min = j

        mark[i], mark[min] = mark[min], mark[i]
        id[i], id[min] = id[min], id[i]
    
    for i in range(n):
        f.write(f'Id:{id[i]} Mark:{mark[i]}\n')