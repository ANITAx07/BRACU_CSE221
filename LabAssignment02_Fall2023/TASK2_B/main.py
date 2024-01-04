with open('TASK2_A\Input.txt', 'r') as abc :
    var=abc.readlines()
    f=open('E:\A2\TASK2_B\output.txt', 'w')
    size1,size2=var[0],var[2]  
    lst1=(var[1].strip().split())
    lst2=(var[3].strip().split())
    
    sorted_list=[]  
    i=0
    j=0
    
    while i<int(size1) and j<int(size2):
        
        if int(lst1[i]) < int(lst2[j]):
            sorted_list.append(lst1[i])
            i+=1
        
        elif int(lst1[i]) > int(lst2[j]):
            sorted_list.append(lst2[j])
            j+=1
        
        elif int(lst1[i]) == int(lst2[j]):
            sorted_list.append(lst1[i])
            sorted_list.append(lst2[j])
            i+=1
            j+=1    
    
    if i < int(size1)-1:
        sorted_list += lst1[i+1:]
    else:
        sorted_list += lst2[j+1:]

for k in sorted_list:
    f.write(str(k)+ ' ')   
    