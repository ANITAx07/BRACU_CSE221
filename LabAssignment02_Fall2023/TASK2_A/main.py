##task2(A)
with open('E:\A2\TASK2_A\Input.txt', 'r') as abc :
    var=abc.readlines()
    size1,size2=var[0],var[2]
    f=open("E:\A2\TASK2_A\output.txt","w")
    lst1=var[1].strip().split()
    lst2=var[3].strip().split()
    merged_list=lst1+lst2
    for i in range(len(merged_list)):
        merged_list[i] = int(merged_list[i])
    merged_list.sort()
    print(merged_list)

for i in merged_list:
    f.write(f"{i} ")



