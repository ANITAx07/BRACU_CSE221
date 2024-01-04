with open('E:\A4\TASK-6\input6_1.txt', 'r') as abc:
    f=open('E:\A4\TASK-6\output.txt', 'w')
    size = abc.readline().split()
    grid = []
    for i in range(int(size[0])):
        g = abc.readline().strip()
        g_l = list(g)
        grid.append(g_l)



def dfs(grid, row, col, visited):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '#' or visited[row][col]:
        return 0
    
    visited[row][col] = True
    diamonds = 0
    
    if grid[row][col] == 'D':
        diamonds = 1
    
    diamonds += dfs(grid, row+1, col, visited)
    diamonds += dfs(grid, row-1, col, visited)
    diamonds += dfs(grid, row, col+1, visited)
    diamonds += dfs(grid, row, col-1, visited)
    
    return diamonds


def max_diamonds(grid,rows,cols):
    visited=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(False)
        visited.append(temp)
    maximum = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.' and not visited[i][j]:
                diamonds = dfs(grid, i, j, visited)
                maximum = max(maximum, diamonds)
    
    return maximum
f.write(str(max_diamonds(grid,int(size[0]),int(size[1])))) 
