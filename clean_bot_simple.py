def nextMove(posr, posc, board):

    x,y=(0,0)
    if board[posr][posc]=='d':
        print("CLEAN")
    else:
        for y1 in range(5):
            for x1 in range(5):
                if board[y1][x1]=='d':
                        y=y1
                        x=x1
                        break
#same line
        if(posr==y):
            if(posc <x):
                print('RIGHT')
            else:
                print('LEFT')
        else:
            if(posr < y):
                print('DOWN')
            else:
                print('UP')

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)