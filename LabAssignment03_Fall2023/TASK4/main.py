with open('E:\A3\TASK4\input.txt', 'r') as abc:
    var=abc.readlines()
    size=int(var[0].strip())
    arr=list(map(int,var[1].strip().split()))
    f=open('E:\A3\TASK4\output.txt', 'w')
    def get_max(arr):
        if len(arr) == 2:
            return arr[0] + (arr[1])**2 
        elif len(arr) == 1:
            return float('-inf')
        mid=len(arr)//2
        left_val = get_max(arr[ :mid])
        right_val = get_max(arr[mid: ])

        left_arr = arr[ :mid]
        right_arr = arr[mid:]
        left_max = max(left_arr)
        
        for i in range(len(right_arr)):
            right_arr[i] = right_arr[i]**2  
        right_max = max(right_arr)
        total = left_max + right_max 
        return max(left_val,right_val,total)

f.write(f"{str(get_max(arr))}")