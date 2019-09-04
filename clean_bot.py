#!/usr/bin/python

# Head ends here
from math import sqrt

def euclidean_dist(x1,y1,x2,y2):
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2))

def next_move(posr, posc, board):

    x,y=(0,0)
    shor_dist=100
    if board[posr][posc]=='d':
        print("CLEAN")
    else:
        for y1 in range(5):
            for x1 in range(5):
                if board[y1][x1]=='d':
                    dist=euclidean_dist(x1,y1,posc,posr)
                    if dist < shor_dist and not(x1==posc and y1==posr):
                        shor_dist=dist
                        y=y1
                        x=x1
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




    # else:
    #     if (posc + 1) < 5 and ('d' in board[posr]) and (board[posr].index('d') == posc + 1):
    #         print('RIGHT')
    #     else:
    #         if (posc + 1) > -1 and 'd' in board[posr] and board[posr].index('d') == posc - 1:
    #             print('LEFT')
    #         else:
    #             if (posr + 1) < 5 and 'd' in board[posr + 1] and board[posr + 1].index('d') == posc:
    #                 print('DOWN')
    #             else:
    #                 if (posr - 1) > -1 and 'd' in board[posr - 1] and board[posr - 1].index('d') == posc:
    #                     print('UP')
    #                 else:
    #                     if posc+1 < 5:
    #                         print('RIGHT')
    #                     else:
    #                         if posr+1 < 5:
    #                             print('DOWN')
    #                         else:
    #                             if posc-1 > 0:
    #                                 print('LEFT')
    #                             else:
    #                                 print('UP')

# Tail starts here



if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)