#!/usr/bin/p_y_thon3

'''
this is Sudoku code via z_x_w
'''

import sys

def fun(_x_, _y_):
    '''
    确定行列上不重复
    :param inde__x_:
    :param _y_:
    :param num:
    :return:
    '''

    for _i_ in range(M):
        if _i_ != _x_ and DATA[_i_][_y_] == DATA[_x_][_y_]:
            return 0
    for j in range(M):
        if j != _y_ and DATA[_x_][j] == DATA[_x_][_y_]:
            return 0
    _a_ = 0
    _b_ = 0
    _a_, _b_, _c_, _r_ = new_locate(_x_, _y_, _a_, _b_)
    for _i_ in range(_a_, _a_ + _c_):
        for j in range(_b_, _b_ + _r_):
            if _i_ != _x_ and j != _y_ and DATA[_i_][j] == DATA[_x_][_y_]:
                return 0
    return 1


def new_locate(_x_, _y_, _a_, _b_):
    '''
    新版定位
    :param _x_:
    :param _y_:
    :return:
    '''
    if M % 3 == 0:
        _c_ = 3
        _r_ = int(M / 3)
    elif M % 2 == 0:
        _c_ = 2
        _r_ = int(M / 2)
    _a_ = int(_x_ // _c_ * _c_)
    _b_ = int(_y_ // _r_ * _r_)
    return _a_, _b_, _c_, _r_


# def locate(_x_, _y_, _a_, _b_):
#     '''
#     确定当前元素所在九宫格位置
#     :param _x_:
#     :param _y_:
#     :param a:
#     :param b:
#     :return:
#     '''
#     if 0 <= _x_ < 3 and 0 <= _y_ < 3:
#         _a_ = 0
#         _b_ = 0
#
#     if 3 <= _x_ < 6 and 0 <= _y_ < 3:
#         _a_ = 3
#         _b_ = 0
#
#     if 6 <= _x_ < 9 and 0 <= _y_ < 3:
#         _a_ = 6
#         _b_ = 0
#
#     if 0 <= _x_ < 3 and 3 <= _y_ < 6:
#         _a_ = 0
#         _b_ = 3
#
#     if 0 <= _x_ < 3 and 6 <= _y_ < 9:
#         _a_ = 0
#         _b_ = 6
#
#     if 3 <= _x_ < 6 and 3 <= _y_ < 6:
#         _a_ = 3
#         _b_ = 3
#
#     if 3 <= _x_ < 6 and 6 <= _y_ < 9:
#         _a_ = 3
#         _b_ = 6
#
#     if 6 <= _x_ < 9 and 3 <= _y_ < 6:
#         _a_ = 6
#         _b_ = 3
#
#     if 6 <= _x_ < 9 and 6 <= _y_ < 9:
#         _a_ = 6
#         _b_ = 6
#     return _a_, _b_


def disp():
    '''
    打印结果
    :return:
    '''

    for _i_ in range(M):
        for j in range(M):
            print(DATA[_i_][j], end=' ')
            OP.write(str(DATA[_i_][j]) + ' ')
        print('')
        OP.write('\n')


def dfs(_x_, _y_):
    '''
    深搜
    :param _x_:
    :param _y_:
    :return:
    '''

    if _x_ > M - 1:
        disp()
    elif DATA[_x_][_y_] != 0:
        if _y_ == M - 1:
            dfs(_x_ + 1, 0)
        else:
            dfs(_x_, _y_ + 1)
    else:
        for _i_ in range(1, M + 1):
            DATA[_x_][_y_] = _i_
            if fun(_x_, _y_) == 1:
                if _y_ == M - 1:
                    dfs(_x_ + 1, 0)
                else:
                    dfs(_x_, _y_ + 1)
        DATA[_x_][_y_] = 0


N = int(sys.argv[4])
M = int(sys.argv[3])
IN_FILE = sys.argv[1]
OUT_FILE = sys.argv[2]
DATA = []
FP = open(IN_FILE)
OP = open(OUT_FILE, 'w+')
for line in FP.readlines():
    arr = line.strip().split(" ")
    if arr[0] >= '0':
        int_arr = list(map(int, arr))
        DATA.append(int_arr)
FP.close()
for i in range(N):
    if i > 0:
        DATA[M * (i - 1):M * i] = DATA[M * i:M * (i + 1)]
        print('')
        OP.write('\n')
    dfs(0, 0)
OP.close()
