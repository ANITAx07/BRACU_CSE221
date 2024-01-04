with open("TASK1_A\Input1.txt", "r") as abc:
    var=abc.readline().split()
    # print(type(var))
    size,target_sum=var
    lst=abc.readline().split()
    # print(lst)
    size=int(size)
    a=[]
    f=open('TASK1_A\Output.txt', 'w')
    flag=False
    for i in range(size) :          
        sum=0
        if flag ==True:
            break
        for j in range(i+1, size):
            sum=int(lst[i]) + int(lst[j])
            if sum == int(target_sum):
                a.append(i+1)
                a.append(j+1)
                flag=True
                break
    if flag == False:
        f.write("IMPOSSIBLE")        
            # print(a)
            
    for i in a:
        f.write(str(i) + ' ')