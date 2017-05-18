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


board_size = 19  # the board is 19x19


class Board:
    # to display the board in terminal


    current_state = zeros([board_size,board_size], dtype=np.int)


    def __init__(self, bdst = zeros([board_size,board_size])):
        # bdst is the inputing board-state
        self.current_state = bdst.copy()


    def setto(self, bdst):
        self.current_state = bdst.copy()


    def reset(self):
        self.current_state = zeros([board_size,board_size], dtype=np.int)


    def get(self):
        return self.current_state.copy()


    def display(self):
        """
        to draw the board on the screen, and put pieces in.
        x is the piece positions of the first player (black, moves first)
        o is the second player
        both x and o are len()*2 arrays, meaning [line, col], 1 to 19.
        """

        def array2string(x):
            return ' '.join(x)  # to process string<->array

        edge_char = ' '  # around the board
        grid_char = '.'  # empty on board
        star_char = '+'  # 9 star positions
        fst_char = 'x'
        scd_char = 'o'

        # an empty board with left/right edges
        UI_board = array([ \
                list(str(i).zfill(2)+grid_char*board_size+str(i).zfill(2)) \
                for i in range(board_size+2) ])

        # polish the stars
        UI_board[ 4, 5] = star_char
        UI_board[ 4,-6] = star_char
        UI_board[-5, 5] = star_char
        UI_board[-5,-6] = star_char
        UI_board[10,11] = star_char
        UI_board[ 4,11] = star_char
        UI_board[10,-6] = star_char
        UI_board[-5,11] = star_char
        UI_board[10, 5] = star_char

        # polish the upper/bottom edges
        #UI_board[0] = UI_edge_char
        #UI_board[-1] = UI_edge_char
        for i in range(board_size):
            UI_board[0, i+2] = string.ascii_uppercase[i]
            UI_board[-1,i+2] = string.ascii_uppercase[i]

        # polish the corners
        UI_board[0, 0] = edge_char
        UI_board[0, 1] = edge_char
        UI_board[-1,0] = edge_char
        UI_board[-1,1] = edge_char
        UI_board[0, -1] = edge_char
        UI_board[0, -2] = edge_char
        UI_board[-1,-1] = edge_char
        UI_board[-1,-2] = edge_char

        for i0,i1 in muloop([board_size, board_size]):
            if self.current_state[i0,i1] == 1:
                UI_board[i0+1,i1+2] = fst_char  # y add 1 for edges
            elif self.current_state[i0,i1] == 2:
                UI_board[i0+1,i1+2] = scd_char  # y add 1 for edges

        os.system('clear')
        print()
        print()
        for i in UI_board:
            print(array2string(i).center(1))
        print()


    def put_piece(self, pos, player):
        # pos is the position to put new piece
        # player is 1 or 2 meaning who put the piece
        x0,x1 = pos
        if self.current_state[x0,x1] != 0: # the position has been occupied
            return False
        self.current_state[x0,x1] = player
        print(self.cluster_4direct(pos, player))
        self.display()
        return True


    def cluster_1direct(self, pos, player, flag):
        # to get the cluster of given direction (flag)
        # of the given position (pos)
        # only collect the opposite player's pieces
        if player == 1:
            opst = 2
        elif player == 2:
            opst = 1
        else:
            return False
        #
        x0,x1 = pos
        if flag=='L' or flag=='l':
            if x0<=0: return False
            if self.current_state[x0-1, x1] != opst: return False
            clus = [ [x0-1,x1] ]
            tobe_proc = [ [x0-1,x1] ]
        if flag=='R' or flag=='r':
            if x0>=(board_size-1): return False
            if self.current_state[x0+1, x1] != opst: return False
            clus = [ [x0+1,x1] ]
            tobe_proc = [ [x0+1,x1] ]
        if flag=='U' or flag=='u':
            if x1<=0: return False
            if self.current_state[x0, x1-1] != opst: return False
            clus = [ [x0,x1-1] ]
            tobe_proc = [ [x0,x1-1] ]
        if flag=='D' or flag=='d':
            if x0>=(board_size-1): return False
            if self.current_state[x0, x1+1] != opst: return False
            clus = [ [x0,x1+1] ]
            tobe_proc = [ [x0,x1+1] ]
        #
        while len(tobe_proc)>0:
            x0,x1 = tobe_proc.pop(0)  # get the queue head
            if x0>0:
                if self.current_state[x0-1, x1] == opst \
                and [x0-1, x1] not in clus:
                    clus.append([x0-1, x1])
                    tobe_proc.append([x0-1, x1])
            if x0<(board_size-1):
                if self.current_state[x0+1, x1] == opst \
                and [x0+1, x1] not in clus:
                    clus.append([x0+1, x1])
                    tobe_proc.append([x0+1, x1])
            if x1>0:
                if self.current_state[x0, x1-1] == opst \
                and [x0, x1-1] not in clus:
                    clus.append([x0, x1-1])
                    tobe_proc.append([x0, x1-1])
            if x1<(board_size-1):
                if self.current_state[x0, x1+1] == opst \
                and [x0, x1+1] not in clus:
                    clus.append([x0, x1+1])
                    tobe_proc.append([x0, x1+1])
        return clus


    def cluster_4direct(self, pos, player):
        # to get the cluster of all the 4 directions
        # and merge them together
        x = []
        #
        y1 = self.cluster_1direct(pos, player, 'L')
        y2 = self.cluster_1direct(pos, player, 'R')
        y3 = self.cluster_1direct(pos, player, 'U')
        y4 = self.cluster_1direct(pos, player, 'D')
        #
        if y1 != False and y2 != False:
            if y1[0] in y2: y2 = False
        if y1 != False and y3 != False:
            if y1[0] in y3: y3 = False
        if y1 != False and y4 != False:
            if y1[0] in y4: y4 = False
        if y2 != False and y3 != False:
            if y2[0] in y3: y3 = False
        if y2 != False and y4 != False:
            if y2[0] in y4: y4 = False
        if y3 != False and y4 != False:
            if y3[0] in y4: y4 = False
        #
        for i in [y1,y2,y3,y4]:
            if i != False:
                x.append(i)
        return x


    def if_qi(clus):
        # if the given cluster has at least 1 qi
        return


    def capture(self, clus):
        # if there are pieces to remove, for the new put piece
        # at position pos, put by the player
        return


if __name__ == "__main__":
    x=array([[6,4], [3,3], [1,8], [4,3], [1,19], [3,4], [12,1]])
    o=array([[2,1], [1,7], [3,5], [3,6], [1,3], [19,4], [16,4]])

    bdst = zeros([board_size, board_size])
    for i0,i1 in x: bdst[i0-1,i1-1] = 1  # -1 to convert to matrix
    for i0,i1 in o: bdst[i0-1,i1-1] = 2  #    to count from 0

    bd = Board()
    bd.setto(bdst)
    bd.display()
