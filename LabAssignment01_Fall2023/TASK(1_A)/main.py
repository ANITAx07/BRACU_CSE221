with open ("INPUT1(A).txt","r") as abc:
    var=abc.readlines()
    print(var)
    l=len(var)
    f2=open("OUTPUT1(A).txt", 'w')  
    for i in range(1,l):
        i=int(var[i])
        if int(i)%2 == 0:
            f2.write(f"{i} is an Even number.\n")
        else:
            f2.write(f"{i} is an Odd number.\n")
          
