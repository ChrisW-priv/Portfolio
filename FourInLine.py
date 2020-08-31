import os

class FourInLine:
    def __init__(self):
        self.board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    def __repr__(self):
        str_grid = "1   2   3   4   5   6   7 \n-   -   -   -   -   -   -\n"
        for i in range(len(self.board)):
            if i % 1 == 0 and i != 0:
                str_grid += ("- - - - - - - - - - - - -\n")
            for j in range(len(self.board[0])):
                if j % 1 == 0 and j != 0:
                    str_grid += (" | ")
                if j == 6:
                    str_grid += str((self.board[i][j])) + '\n'
                else:
                    str_grid += (str(self.board[i][j]) + "")
        return str_grid

    def check_lines(self):
        b = self.board # makes writing code bit more faster
        # horisontal_line
        horizontal_line = lambda row, column: True if (b[row][column]==b[row][column+1]==b[row][column+2]==b[row][column+3]!=' ') else False  
        # vertical_line
        vertical_line = lambda row, column: True if (b[row][column]==b[row+1][column]==b[row+2][column]==b[row+3][column]!=' ') else False
        # diagonal_line
        diagonal_right_line = lambda row, column: True if (b[row][column]==b[row+1][column+1]==b[row+2][column+2]==b[row+3][column+3]!=' ') else False
        # diagonal_line
        diagonal_left_line = lambda row, column: True if (b[row][column]==b[row+1][column-1]==b[row+2][column-2]==b[row+3][column-3]!=' ') else False

        horizontal_lines = [horizontal_line(row,col) for row in range(6) for col in range(4)]
        vertical_lines = [vertical_line(row,col) for row in range(3) for col in range(7)]
        diagonal_right_lines = [diagonal_right_line(row,col) for row in range(3) for col in range(4)]
        diagonal_left_lines = [diagonal_left_line(row,col) for row in range(3) for col in range(4,7)]

        lines = horizontal_lines+vertical_lines+diagonal_right_lines+diagonal_left_lines

        return True in lines

    def highest(self):
        highest = []
        for column in range(len( self.board[0] )):
            for row in range(len( self.board )):
                if self.board[len( self.board )-row-1][column] == " ":
                    highest.append(row);break
                if row == 5:
                    highest.append(row+1);break
        return highest

    def move(self, move, player):
        highest = self.highest()

        if highest[move] == 6:
            raise MoveNotValidError('This column is full, choose other one\n')
        else:
            self.board[len( self.board )-highest[move]-1][move] = player

    def play(self):
        os.system('cls')
        print(self)

        stop = False
        while not stop:
            for player in ['X', 'O']:
                move_ok=False
                while not move_ok:
                    
                    move = input(f'What is ur move? ({player})\n > ')
                    try:
                        assert int(move) in range(1,7+1)
                        self.move(int(move)-1, player)
                    
                    except MoveNotValidError as e:
                        print(e)
                    except ValueError:
                        print('This is not a number from 1 to 7!')
                    except AssertionError:
                        print('not in range 1-7')
                    
                    else:
                        os.system('cls')
                        print(self)
                        move_ok=True
                
                if self.check_lines():
                    print(f'\nPlayer "{player}" wins!')
                    stop = True
                    break

class MoveNotValidError(Exception):
    def __init__(self, msg):
        self.message = msg

if __name__ == '__main__':
    try:
        game = FourInLine()
        print(game.play())
    except KeyboardInterrupt:
        print('\nYou have quit the game!')
