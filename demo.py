#!/usr/bin/python3


'''
pylint demo code
'''


def compare(num1, num2):

    '''
    pylint demo code
    '''
    if num1 > num2:
        return num2
    return num1


def search(index_x, index_y, count):
    '''
    pylint demo code
    '''
    global _MIN_
    global MAZE
    global N
    if index_x == N - 2 and index_y == N - 2:
        _MIN_ = compare(_MIN_, count)
    else:
        MAZE[index_x][index_y] = 1
        if index_y < N - 1 and MAZE[index_x][index_y + 1] == 0:
            search(index_x, index_y + 1, count + 1)
        if index_x < N - 1 and MAZE[index_x + 1][index_y] == 0:
            search(index_x + 1, index_y, count + 1)
        if index_x > 1 and MAZE[index_x - 1][index_y] == 0:
            search(index_x - 1, index_y, count + 1)
        if index_y > 1 and MAZE[index_x][index_y - 1] == 0:
            search(index_x, index_y - 1, count + 1)
        MAZE[index_x][index_y] = 0


N = int(input())
_MIN_ = N*N
MAZE = [[0]*N]*N
for i in range(N):
    MAZE[i] = input().split(" ")
    MAZE[i] = [int(j) for j in MAZE[i]]
search(1, 1, 0)
if _MIN_ == N * N:
    print("No solution")
else:
    print(_MIN_)
