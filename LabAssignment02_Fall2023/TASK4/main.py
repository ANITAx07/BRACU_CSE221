with open("TASK4\Input.txt", "r") as abc:
    start=[]
    end=[] 
    var=abc.readlines()
    # print(var)
    f=open("TASK4\output.txt", "w")
    b=var[0].split()
    # print(b)
    task=int(b[0]) 
    person=int(b[1]) 
    
    for i in range(1, len(var)):
        a=var[i].split(' ')
        start.append(int(a[0]))
        end.append(int(a[1].strip()))
      
    for i in range(task):
        for j in range(task-i-1):
            if end[j] > end[j+1]:
                end[j], end[j+1] = end[j+1], end[j]
                start[j], start[j+1] = start[j+1], start[j]
   
    lst=[]
    for i in range(0,len(start)):
        lst.append((int(start[i]), int(end[i])))
    print(lst)  


    available_p=[0]*person #[0,0]
    com=[]
    counter=0
    for i in range(task):
        for j in range(person):
            for k in range(i,task):
                if lst[k][0] == available_p[j] and i not in com:
                    available_p[j] = lst[i][1]
                    counter+=1  
                    com.append(i)
                    break        
            if lst[i][0] > available_p[j] and i not in com:
                    available_p[j] = lst[i][1]
                    counter+=1  
                    com.append(i)
                    break     
f.write(f'{counter}\n')
    
    