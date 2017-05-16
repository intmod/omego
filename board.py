#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

#  ==============================================
#  ·
#  · Author: Mogei Wang
#  ·
#  · MogeiWang@GMail.com
#  ·
#  · Filename: myBoard.py
#  ·
#  · COPYRIGHT 2017
#  ·
#  · Description: draw ASCII gogame board in term
#  ·
#  ==============================================


UI_board_size = 19  # the board is 19x19
UI_edge_char = ' '  # around the board
UI_grid_char = '.'  # empty on board
UI_star_char = '+'  # 9 star positions
UI_star_position = [4,10,16]


def UI_array2string(x): return ' '.join(x)  # to process string<->array


def UI_draw_board():
    # an empty board with left/right edges
    UI_board = array([ \
             list(str(i).zfill(2)+UI_grid_char*UI_board_size+str(i).zfill(2)) \
             for i in range(UI_board_size+2) ])

    # polish the stars
    for i in itertools.product(UI_star_position, repeat=2):
        UI_board[i] = UI_star_char

    # polish the upper/bottom edges
    #UI_board[0] = UI_edge_char
    #UI_board[-1] = UI_edge_char
    for i in range(UI_board_size):
        UI_board[0, i+2] = string.ascii_uppercase[i]
        UI_board[-1,i+2] = string.ascii_uppercase[i]

    # polish the corners
    UI_board[0, 0] = UI_edge_char
    UI_board[0, 1] = UI_edge_char
    UI_board[-1,0] = UI_edge_char
    UI_board[-1,1] = UI_edge_char
    UI_board[0, -1] = UI_edge_char
    UI_board[0, -2] = UI_edge_char
    UI_board[-1,-1] = UI_edge_char
    UI_board[-1,-2] = UI_edge_char

    os.system('clear')

    print()
    print()
    for i in UI_board:
        print(UI_array2string(i).center(1))
    print()


if __name__ == "__main__": UI_draw_board()
