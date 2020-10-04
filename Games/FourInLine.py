import os
import numpy as np

class FourInLine:
    def __init__(self):
        self.board = np.ndarray(shape=(6,7), dtype=str)

    def __repr__(self):
        str_grid = "1   2   3   4   5   6   7 \n-   -   -   -   -   -   -\n"
        for i in range(len(self.board)):
            if i % 1 == 0 and i != 0:
                str_grid += ("- - - - - - - - - - - - -\n")
            for j in range(len(self.board[0])):
                if j % 1 == 0 and j != 0:
                    str_grid += (" | ")
                if self.board[i][j] == '':
                    str_grid+=' '
                if j == 6:
                    str_grid += str((self.board[i][j])) + '\n'
                else:
                    str_grid += (str(self.board[i][j]) + "")
        return str_grid

    def check_lines(self):
        b = self.board # makes writing code bit more easies
        # horisontal_line
        horizontal_line = lambda row, column: True if (b[row][column]==b[row][column+1]==b[row][column+2]==b[row][column+3]!='') else False  
        # vertical_line
        vertical_line = lambda row, column: True if (b[row][column]==b[row+1][column]==b[row+2][column]==b[row+3][column]!='') else False
        # diagonal_line
        diagonal_right_line = lambda row, column: True if (b[row][column]==b[row+1][column+1]==b[row+2][column+2]==b[row+3][column+3]!='') else False
        # diagonal_line
        diagonal_left_line = lambda row, column: True if (b[row][column]==b[row+1][column-1]==b[row+2][column-2]==b[row+3][column-3]!='') else False

        horizontal_lines = [horizontal_line(row,col) for row in range(b.shape[0]) for col in range(b.shape[1]-3)]
        vertical_lines = [vertical_line(row,col) for row in range(b.shape[0]-3) for col in range(b.shape[1])]
        diagonal_right_lines = [diagonal_right_line(row,col) for row in range(b.shape[0]-3) for col in range(b.shape[1]-3)]
        diagonal_left_lines = [diagonal_left_line(row,col) for row in range(b.shape[0]-3) for col in range(b.shape[1]-3,b.shape[1])]

        lines = horizontal_lines+vertical_lines+diagonal_right_lines+diagonal_left_lines

        return True in lines

    def highest(self):
        highest = []
        for column in range( self.board.shape[1] ):
            for i, row in enumerate(self.board):
                if row[column] != '':
                    highest.append(i);break
                if i == self.board.shape[0]-1:
                    highest.append(5);break
        print(highest)
        return highest

    def move(self, move, player):
        highest = self.highest()

        if highest[move] == self.board.shape[0]:
            raise MoveNotValidError('This column is full, choose other one\n')
        else:
            print('x,y', len( self.board )-highest[move]-1, move)
            self.board[self.board.shape[0]-highest[move]-1][move] = player

    def play(self):
        os.system('cls')
        print(self)

        while True:
            for player in ['X','O']:
                move_ok=False
                while not move_ok:
                    
                    move = input(f'What is ur move? ({player})\n > ')
                    try:
                        assert int(move) in range(1,7+1)
                        self.move( int(move)-1, player )
                    
                    except MoveNotValidError as e:
                        print(e)
                    except ValueError:
                        print('This is not a number from 1 to 7!')
                    except AssertionError:
                        print('not in range 1-7')
                    
                    else:
                        # os.system('cls')
                        print(self.board)
                        move_ok=True
                
                if self.check_lines():
                    print(f'\nPlayer "{player}" wins!')
                    return

class MoveNotValidError(Exception):
    def __init__(self, msg):
        self.message = msg

if __name__ == '__main__':
    game = FourInLine()
    # print(game.board)
    try:
        game.play()
        print(game.board)

    except KeyboardInterrupt:
        print('\nYou have quit the game!')
