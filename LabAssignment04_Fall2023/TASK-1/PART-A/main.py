# import numpy as np
with open('\TASK-1\PART-A\input1a_1.txt', 'r') as abc:
   var=abc.readline().split("\n")
   f=open('TASK-1\PART-A\output1a_1.txt', 'w')
   m=var[0].split(' ')
   vertices=int(m[0])
   edges=int(m[1])
   adj_mat=[]
   for i in range(vertices+1):
      adj_mat1=[0]*(vertices+1)
      adj_mat.append(adj_mat1[:])
   print(adj_mat)
   for j in range(edges):
      st,end,weight = [int(i) for i in abc.readline().split(' ')]
      adj_mat[st][end] = weight
   
   for i in range(vertices+1):
      for j in range(vertices+1):
          f.write(f'{adj_mat[i][j]} ')
      f.write('\n')