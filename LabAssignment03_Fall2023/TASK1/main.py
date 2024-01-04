with open('TASK1\Input.txt', "r") as abc:
    var=abc.readlines()
    size=int(var[0])
    # print(size)
    arr=var[1].strip().split()
    # print(arr)
    f=open('TASK1\Output.txt','w')
    def merge(a, b):
        i,j=0,0
        sorted_list=[]
        length=len(a)+len(b)
        for k in range(length):

            if i<len(a) and j<len(b):
                if int(a[i]) < int(b[j]):
                    sorted_list.append(a[i])
                    i+=1
                else:
                    sorted_list.append(b[j])
                    j+=1
            else:
                if i < len(a):
                    sorted_list.append(a[i])
                    i+=1
                else:
                    sorted_list.append(b[j])
                    j+=1
        return sorted_list

    def mergeSort(arr):
        if len(arr)<= 1:
           return arr
        else:
            mid = len(arr)//2
            a1 = mergeSort(arr[ :mid])
            a2 = mergeSort(arr[mid: ])
            return merge(a1, a2)
    x=mergeSort(arr)
for i in x:
   f.write(str(i)+' ')