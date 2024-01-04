with open('TASK2\Input.txt', "r") as abc:
    var=abc.readlines()
    size=int(var[0])
    array=var[1].strip().split()
    f=open('TASK2\output.txt','w')

    def mergeSort(array):
        if len(array)<= 1:
            return int(array[0])
        else:
            mid = len(array)//2
            a1 = mergeSort(array[ :mid])
            a2 = mergeSort(array[mid: ])
            if int(a1) > int(a2):
                return a1
            else:
                return a2
    y=mergeSort(array)
f.write(str(y))