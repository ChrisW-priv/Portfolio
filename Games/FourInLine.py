import os
import numpy as np
import pygame


class FourInLine:
	def __init__(self, size=20):
		self.board = np.empty(shape=(6,7), dtype=str)
		self.moves=[]

		self.shape = self.board.shape[::-1]
		self.blockSize = size
		self.BLACK = (0, 0, 0)
		self.WHITE = (200, 200, 200)

	def init_screen(self):
		pygame.init()
		self.font = pygame.font.SysFont('Arial', 18)
		pygame.display.set_caption('Four In Line')
		self.screen = pygame.display.set_mode( (self.shape[0]*self.blockSize, self.shape[1]*self.blockSize) )
		self.screen.fill(self.WHITE)
		pygame.display.update()

	def drawGrid(self):
		Red = (200, 100, 100)
		Blue = (0, 200, 200)

		for x in range(self.shape[0]):
			for y in range(self.shape[1]):
				px = x*self.blockSize
				py = y*self.blockSize
				rect = pygame.Rect(px, py, self.blockSize, self.blockSize)
				pygame.draw.rect(self.screen, self.BLACK, rect, 1)
				# self.screen.blit(self.font.render(self.board[y][x], False, self.BLACK), (px+6, py+1))
				
				if self.board[y][x] == 'X':
					pygame.draw.circle(self.screen, Red, (px+self.blockSize//2,py+self.blockSize//2), self.blockSize//2)
				if self.board[y][x] == 'O':
					pygame.draw.circle(self.screen, Blue, (px+self.blockSize//2,py+self.blockSize//2), self.blockSize//2)
		pygame.display.update()

	def play(self):
		self.init_screen()
		self.drawGrid()

		while True:
			for player in ['X','O']:
				move_ok=False
				while not move_ok:
					for event in pygame.event.get():
						# if clicks close
						if event.type == pygame.QUIT:
							self.quit()
						# each mouse click will be couted as a move
						elif event.type == pygame.MOUSEBUTTONDOWN:
							move = pygame.mouse.get_pos()[0]//self.blockSize
							move_ok=self.move( move, player )
						# if makes mistake use keyboard to move undo last move
						elif event.type == pygame.KEYDOWN:
							self.move_back()
							move_ok=True
						
				if self.check_lines():
					self.win_screen(player)
					return

	def quit(self):
		from sys import exit
		pygame.quit()
		exit()

	def move(self, move, player):
		try:
			highest = self.highest()

			if highest[move] == self.board.shape[0]:
				raise MoveNotValidError('This column is full, choose other one\n')
			else:
				x=self.board.shape[0]-highest[move]-1
				y=move
				self.board[x][y] = player
				self.moves.append( (x,y) )
		except MoveNotValidError as e:
			print(e)
			return False
		else:
			self.drawGrid()
			return True
		
	def move_back(self):
		try:
			last_move = self.moves.pop(-1)
		except IndexError:
			pass
		else:
			# clear board
			lx,ly=last_move
			self.board[lx][ly]=''
			self.init_screen()
			self.drawGrid()

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
		for column in range(len( self.board[0] )):
			for row in range( len(self.board) ):
				if self.board[len( self.board )-row-1][column] == "":
					highest.append(row);break
				if row == 5:
					highest.append(row+1);break
		return highest

	def win_screen(self, winner):
		print(f'\nPlayer "{winner}" wins!')
		pygame.init()
		font = pygame.font.SysFont('Arial', 18)
		pygame.display.set_caption('Box Test')
		screen = pygame.display.set_mode( (self.shape[0]*self.blockSize, self.shape[1]*self.blockSize) )
		screen.fill(self.WHITE)
		if winner == 'X':
			winner='Red'
		else:
			winner='Blue'
		screen.blit(self.font.render(f'Player "{winner}" wins!', False, self.BLACK), (10, 10))
		pygame.display.update()


class MoveNotValidError(Exception):
	def __init__(self, msg):
		self.message = msg

if __name__ == '__main__':
	game = FourInLine(40)
	try:
		game.play()
	except KeyboardInterrupt:
		print('\nYou have quit the game!')
