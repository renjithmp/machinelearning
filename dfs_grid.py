#Your task is to complete the function dfs that takes in r,c as the grid size, pacman_r and pacman_c which is the position of Pacman and food_r and food_c as the position of food and the grid as input and print the output in the required format.
def dfs_grid(r,c,pacman_r,pacman_c,food_r,food_c,grid):
    stack=[]
    parent=[]
    path=[]
    visited=[]
    explored=[]
    y=pacman_r
    x=pacman_c
    visited.append((y, x))
    stack.append((y, x))
    explored.append((y, x))
    E=0
    while True:
        #print(y,x)
        if y==food_r and x==food_c:
            path.append((y,x))
            while(True):
                for obj in parent:
                    (y_t,x_t)=obj["node"]
                    if y_t==y and x_t==x:
                        (y1, x1) = obj["parent"]
                        path.append((y1, x1))
                        y=y1
                        x=x1
                        break
                if(y1==pacman_r and x1==pacman_c):
                    break

            break
        else:
            if y - 1 >= 0 and grid[y - 1][x] != '%' and not (y - 1, x) in visited:
                stack.append({"node":(y-1,x),"parent":(y,x)})
                #path.append({(y,x):(y-1,x)})
            if x - 1 >= 0 and grid[y][x - 1] != '%' and not (y, x - 1) in visited:
                stack.append({"node":(y,x-1),"parent":(y,x)})
            if x + 1 < c and grid[y][x + 1] != '%' and not (y, x + 1) in visited:
                stack.append({"node":(y,x+1),"parent":(y,x)})
            if y+1 <r and grid[y+1][x]!='%'and not (y+1,x) in visited:
                stack.append({"node":(y+1,x),"parent":(y,x)})

        obj=stack.pop()
        (y,x)=obj["node"]
        if (y,x) not in visited:
            visited.append((y,x))
            parent.append({"parent":(obj["parent"]),"node":(y,x)})

    print(len(visited))
    [print(str(y)+" "+str(x)) for y,x in visited]
    print(len(path)-1)
    for i in range(len(path)):
        (y,x)=path.pop()
        print(str(y)+" "+str(x))
if __name__ == "__main__":
    pacman_pos = [int(i) for i in input().strip().split()]
    food_pos = [int(i) for i in input().strip().split()]
    size = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(size[0])]
    dfs_grid(size[0], size[1],pacman_pos[0],pacman_pos[1],food_pos[0],food_pos[1], board)