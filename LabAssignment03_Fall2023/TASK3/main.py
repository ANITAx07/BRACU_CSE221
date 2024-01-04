with open('E:\A3\TASK3\Input.txt', 'r') as abc:
    var=abc.readlines()
    total_aliens=int(var[0].strip())
    arr=var[1].strip().split()
    f=open('E:\A3\TASK3\output.txt', 'w')
    # print(lst)
    def compare(a, b):
        if a>b:
            return 0
        else:
            return 1
    
    def mergeSort(arr, ref):
        if len(arr) <= 1:
            return compare(arr[0], ref)
        else:
            mid = len(arr)//2
            a1 = mergeSort(arr[:mid],ref) 
            a2 = mergeSort(arr[mid:],ref)  
            return a1+a2
    counter = 0
for i in range(total_aliens-1):
    counter+=mergeSort(arr[i+1:],arr[i])
f.write(str(counter))
       
           
        
    
