with open("TASK(2)\INPUT1.txt","r") as abc:
    var=abc.readlines()
    v=var[1].split(' ')
    #print((v))
    f=open("TASK(2)\OUTPUT1.txt","w")
    print(type(f))
    for i in range(int(var[0])):
        v[i]=int(v[i])
    #print(v)    
    def bubblesort(v):
        for i in range(len(v)-1):
            flag=False
            for j in range(len(v)-i-1):
                if v[j] > v[j+1]:
                    v[j], v[j+1] = v[j+1], v[j]
                    flag=True
            if flag == False:        
                break    
        return v
    for i in (bubblesort(v)):
        f.write(f'{i} ')
## comment 
"""
The given array must already be sorted to be the best case scenario for the bubble sort.
I'm using a flag to determine if the array is sorted or not. 
If the given array is sorted, there won't be any swapping; we'll be able to tell by our flag after only once traversing the array, at which point we'll end the outer loop.
This has an O(n) time complexity because the array is only traversed once.
"""


