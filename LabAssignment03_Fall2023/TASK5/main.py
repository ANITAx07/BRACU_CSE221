with open('E:\A3\TASK5\input.txt', 'r') as abc:
    var=abc.readlines()
    size=int(var[0].strip())
    arr=var[1].strip().split()
    f=open('E:\A3\TASK5\output.txt', 'w')

    def partition(arr,l,h):
      pivot = arr[h]
      x = l - 1
      for i in range(l,h):
            if arr[i] <= pivot:
                  x+=1
                  arr[x],arr[i] = arr[i],arr[x]
      arr[x+1],arr[h] = arr[h],arr[x+1]
      return x+1
      
    def quicksort(a, l, h):
        if l < h:
            p = partition(a,l,h)
            quicksort(a,l,p-1)
            quicksort(a,p+1,h)

quicksort(arr,0,size-1)   
# print(arr)        
f.write(' '.join(arr))          