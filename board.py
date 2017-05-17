#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

#  ==============================================
#  ·
#  · Author: Mogei Wang
#  ·
#  · MogeiWang@GMail.com
#  ·
#  · Filename: board.py
#  ·
#  · COPYRIGHT 2017
#  ·
#  · Description: draw ASCII gogame board in term
#  ·
#  ==============================================


UI_board_size = 19  # the board is 19x19


def UI_array2string(x): return ' '.join(x)  # to process string<->array


def UI_draw_board(x, o):
    """
      to draw the board on the screen, and put pieces in.
      x is the piece positions of the first player (black, moves first)
      o is the second player
      both x and o are len()*2 arrays, meaning [line, col], 1 to 19.
    """

    UI_edge_char = ' '  # around the board
    UI_grid_char = '.'  # empty on board
    UI_star_char = '+'  # 9 star positions
    UI_1st_char = 'x'
    UI_2nd_char = 'o'

    # an empty board with left/right edges
    UI_board = array([ \
             list(str(i).zfill(2)+UI_grid_char*UI_board_size+str(i).zfill(2)) \
             for i in range(UI_board_size+2) ])

    # polish the stars
    UI_board[ 4, 5] = UI_star_char
    UI_board[ 4,-6] = UI_star_char
    UI_board[-5, 5] = UI_star_char
    UI_board[-5,-6] = UI_star_char
    UI_board[10,11] = UI_star_char
    UI_board[ 4,11] = UI_star_char
    UI_board[10,-6] = UI_star_char
    UI_board[-5,11] = UI_star_char
    UI_board[10, 5] = UI_star_char

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

    for i0,i1 in x:
        if i0<=0 or i>UI_board_size:  # check before plotting
            print("error in board plotting 1st player", i0,i1)
            exit(-1)
        UI_board[i0,i1+1] = UI_1st_char  # y add 1 for edges

    for i0,i1 in o:
        if i0<=0 or i>UI_board_size:
            print("error in board plotting 2nd player", i0,i1)
            exit(-1)
        UI_board[i0,i1+1] = UI_2nd_char  # y add 1 for edges

    os.system('clear')

    print()
    print()
    for i in UI_board:
        print(UI_array2string(i).center(1))
    print()


if __name__ == "__main__":
    x=array([[6,4], [3,3], [1,8], [4,3], [1,12], [3,4], [12,1]])
    o=array([[2,1], [1,7], [3,5], [3,6], [1,3], [18,4], [15,3]])
    UI_draw_board(x,o)
