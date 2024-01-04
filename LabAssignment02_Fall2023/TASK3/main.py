with open("TASK3\input.txt", "r") as abc:
    start=[]
    end=[] 
    var=abc.readlines()
    size=int(var[0])
    var1=var[1:]
    f=open("TASK3\output.txt", "w")
    for i in range(0, size):
        a=var1[i].split(' ')
        start.append(int(a[0]))
        end.append(int(a[1].strip()))
    
    for i in range(0,size):   
        min = i
        for j in range(i+1, size):    
            if end[min] > end[j]:     
                min = j
            if end[min] == end[j]:
                if start[min] < start[j]:
                    min = j
        end[i], end[min] = end[min], end[i]
        start[i], start[min] = start[min], start[i]
    
    current=0  
    lst=[]
    for i in range(size):
        if current <= start[i]:                                       
            current = end[i]
            lst.append(f'{start[i]} {end[i]}')
    
    f.write(f'{len(lst)}\n')
    for i in range(len(lst)):
        f.write(f'{lst[i]}\n')

   

