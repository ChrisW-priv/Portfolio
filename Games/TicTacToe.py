import os


class TicTacToe:
    def __init__(self):
        self.players = ["X","O"]
        self.matrix = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:""}
    
    def move(self, pos,player):
        if self.matrix[pos] == "":
            self.matrix[pos] = player
        else:
            raise MoveNotValidError('Position already taken try another one')
    
    def check_lines(self):
        lines=[[0,1,2,],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] 
        for line in lines:
            if self.matrix[line[0]]== self.matrix[line[1]]== self.matrix[line[2]]!='':
                return True
    
    def print_current_matrix(self):
        long=5
        middle_line= ('|'+'-'*long+'|')
        def c(n):
            return " " if (self.matrix[n] == "") else self.matrix[n]
        print(middle_line)
        for n in range(3):
            print(f"|{c(n*3)}|{c(n*3+1)}|{c(n*3+2)}|")
            print(middle_line)
    
    def play(self):
        self.print_current_matrix()
        stop = False
        while not stop:
                for player in self.players:
                    move_ok=False
                    while not move_ok:
                        move = input(f'What is ur move? ({player})\n > ')
                        try:
                            assert int(move) in range(1,9+1)
                            self.move(int(move)-1, player)
                        except MoveNotValidError as e:
                            print(e)
                        except ValueError:
                            print('This is not a number from 1 to 9!')
                        except AssertionError:
                            print('not in range 1-9')
                        else:
                            os.system('cls')
                            self.print_current_matrix()
                            move_ok=True
                    if self.check_lines():
                        print(f'\nPlayer "{player}" wins!')
                        stop = True
                        break

    
class MoveNotValidError(Exception):
                def __init__(self, msg):
                    self.message = msg

                                
t = TicTacToe()
t.play()
