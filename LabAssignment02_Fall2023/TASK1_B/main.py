with open("TASK1_B\Input.txt", "r") as abc:
    var=abc.readline().split()
    # print(type(var))
    size,target_sum=var
    lst=abc.readline().split()
    # print(lst)
    size=int(size)
    a=[]
    i=0
    j=len(lst)-1
    f=open('TASK1_B\Output.txt', 'w')
    while (i < j and i!=j):
        if i == j:
            f.write('IMPOSSIBLE')         
            break
        if int(lst[i]) + int(lst[j]) == int(target_sum):
              a.append(i+1)
              a.append(j+1)
              break
        if int(lst[i]) + int(lst[j]) < int(target_sum):
            i+=1
        if int(lst[i]) + int(lst[j]) > int(target_sum):
            j-=1
            
    for k in a:
        f.write(str(k) + ' ')
