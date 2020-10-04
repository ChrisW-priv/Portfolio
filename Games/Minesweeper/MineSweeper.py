import pygame

class MineSweeper:
    def __init__(self, board, n_mines):
        self.board = board
        self.mines = n_mines
        self.shape = board.shape
        self.blockSize = 20
        self.BLACK = (0, 0, 0)
        self.WHITE = (200, 200, 200)
        self.seen = []
        
        self.play()

    def play(self):
        self.drawGrid()        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    import sys
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    px=x//self.blockSize
                    py=y//self.blockSize
                    if event.button==1 and self.board[px][py].flaged == False:
                        self.board[px][py].seen=True
                        self.seen.append( (px,py) )
                        if self.board[px][py].value not in [str(i) for i in range(1,9)]:
                            self.update_all_boxes_around( pos=(px,py) )
                    elif event.button==3 and self.board[px][py].seen == False and self.board[px][py].flaged == False:
                        self.board[px][py].flaged=True
                    elif event.button==3 and self.board[px][py].flaged == True:
                        self.board[px][py].flaged=False
                    self.drawGrid()
                if self.game_over_or_win():
                    return

    def game_over_or_win(self):
        seen=0
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if self.board[x][y].seen == True:
                    seen+=1
                if self.board[x][y].seen == True and self.board[x][y].value == 'BOMB':
                    print('You lost!')
                    return True
                if self.shape[0]*self.shape[1]-seen==self.mines:
                    print('You won!')
                    return True

    def update_all_boxes_around(self,pos):
        px,py = pos
        to_check = [ (-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1) ]
        for check in to_check:
            try:
                cx,cy = check
                nx=px+cx
                ny=py+cy
                if nx<0 or ny<0:
                    continue
                tile = self.board[ nx ][ ny ]
                if tile.value == '0' and (nx,ny) not in self.seen:
                    tile.seen=True
                    self.seen.append( (nx,ny) )
                    self.update_all_boxes_around( pos=(nx,ny) )
                elif tile.value in [str(i) for i in range(1,9)]:
                    tile.seen=True
                    self.seen.append( (nx,ny) ) 
            except IndexError:
                continue
            except AttributeError:
                continue

    def drawGrid(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 18)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((self.shape[0]*self.blockSize, self.shape[1]*self.blockSize))
        self.screen.fill(self.WHITE)
        pygame.display.update()

        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                px = x*self.blockSize
                py = y*self.blockSize
                rect = pygame.Rect(px, py, self.blockSize, self.blockSize)
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)
                
                if self.board[x][y].seen == True:
                    self.screen.blit(self.font.render(self.board[x][y].value[0], False, self.BLACK), (px+6, py+1))
                if self.board[x][y].flaged == True:
                    self.screen.blit(self.font.render('F', False, self.BLACK), (px+6, py+1))

        pygame.display.update()


if __name__ == '__main__':
    from BoardBuilder import BoardBuilder
    shape = (50,25)
    MINES = 10

    board = BoardBuilder(shape=shape, n_mines=MINES)
    # print(board)
    game = MineSweeper(board.matrix, n_mines=MINES)
