with open ("TASK(1_B)\INPUT1(B).txt","r") as abc:
    var=abc.readlines()
    print(var)
    f=open("TASK(1_B)\OUTPUT1(B).txt","w")
   
    for i in range(1,len(var)):
        v=var[i].split(' ')
        op=(v[2])
        
        if op == '+':
            r1=int(v[1]) + int(v[3])
            f.write("The result of " + v[1] + " + "+ str(int(v[3])) +  " is "+ str(r1)+"\n")
           
        if op == '-':
            r1=int(v[1]) - int(v[3])
            f.write("The result of "+ v[1]+ " - "+ str(int(v[3])) + " is "+ str(r1)+"\n")
        
        if op == '/':
            r1=int(v[1]) / int(v[3])
            f.write("The result of "+ v[1]+ " / "+ str(int(v[3])) + " is "+ str(r1)+"\n")
        
        if op == '*':
            r1=int(v[1]) * int(v[3])
            f.write("The result of "+ v[1]+ " * "+ str(int(v[3])) + " is "+ str(r1)+"\n")
    
