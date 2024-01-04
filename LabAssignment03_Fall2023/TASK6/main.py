with open('E:\A3\TASK6\input.txt', 'r') as abc:
    var=abc.readlines()
    total=int(var[0].strip())
    lst=var[1].strip().split()
    # print(var)
    # print(total)
    print(lst)
    query=[]
    i=3
    j=len(var)
    while i < j:
        query.append(var[i].strip())
        i+=1
    print(query)    
    f=open('E:\A3\TASK6\output.txt','w')

    def partition(arr,l,h):
        pivot = int(arr[h])
        x = l-1 
        for i in range(l,h):
              if int(arr[i]) <= pivot:
                    x+=1
                    arr[x],arr[i] = arr[i],arr[x]
        arr[x+1],arr[h] = arr[h],arr[x+1]
        return x+1
    
    def find(arr,k):   #[10 11 10 6 7 9 8 15 2], 5
        i=0
        j=len(arr)-1
        while i<j:
            p=partition(arr,i,j)
            if p == k:
                r=int(arr[p])
                return r-1
            if p > k:
                j=p-1
            else:
                i=p+1     
        return

for i in range(len(query)):
    a=int(query[i])
    kth=find(lst,a) 
    f.write(str(kth)+'\n')

