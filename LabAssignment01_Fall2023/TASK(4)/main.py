with open("TASK(4)\INPUT4.txt", "r") as abc:
    var=abc.readlines()
    # print(var)
    f=open('TASK(4)\OUTPUT4.txt', 'w')
    n=int(var[0])
    # print(n)
    string=[]
    train_name=[]
    time=[]
    for i in range(1,len(var)):
        t=var[i].strip()
        string.append(t)
        train_name.append(t.split()[0])
        time.append(t.split()[-1])
    # print(train_name)   
    # print(time) 
    for i in range(len(train_name)):
        for j in range(len(train_name)-i-1):
            if train_name[j] > train_name[j+1]:
                train_name[j], train_name[j+1] = train_name[j+1], train_name[j]
                string[j], string[j+1] = string[j+1], string[j]

            if train_name[j] == train_name[j+1]:
                if time[j] > time[j+1]:
                    time[j], time[j+1] = time[j+1], time[j]
                    string[j], string[j+1] = string[j+1], string[j]    
    for i in range(n):
        f.write(f"{string[i]}\n")


          