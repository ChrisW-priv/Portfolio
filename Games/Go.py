import numpy as np
import pygame


class Tile:
	def __init__(self, value):
		self.to_be_seen = False
		self.value = str(value)


class Go:
	def __init__(self,shape=(9,9), size = 40):
		self.board = np.empty(shape=shape, dtype=str)
		self.shape = shape
		self.white_prisoners = 0
		self.black_prisoners = 0
		self.white_teritory = 0
		self.black_teritory = 0
		
		self.blockSize = size

	def play(self):
		self.init_board()
		self.drawGrid()

		while True:
			for player in ['W','B']:
				for event in pygame.event.get():
					# if clicks close
					if event.type == pygame.QUIT:
						import sys
						pygame.quit()
						sys.exit()
					# each mouse click will be couted as a move
					elif event.type == pygame.MOUSEBUTTONDOWN:
						move = pygame.mouse.get_pos()
						self.move( move, player )
						self.drawGrid()
						
				if self.game_is_finished():
					self.win_screen(player)
					return

	def decide_winner(self):
		white_score = self.white_prisoners + self.white_teritory
		black_score = self.black_prisoners + self.black_teritory

		if white_score > black_score:
			return 'White'
		elif white_score == black_score:
			return 'Draw'
		else:
			return 'Black'

	def game_is_finished(self):
		pass

	def win_screen(self, player):
		pass

	def move(self, move, player):
		x,y = move
		x = x//self.blockSize
		y = y//self.blockSize
		self.board[x][y] = player

	def init_board(self):
		YELOW = (100,100,100)
		pygame.init()
		pygame.display.set_caption('Box Test')
		self.screen = pygame.display.set_mode((self.shape[0]*self.blockSize, self.shape[1]*self.blockSize))
		self.screen.fill(YELOW)
		pygame.display.update()

	def drawGrid(self):
		BLACK = (0, 0, 0)
		WHITE = (200, 200, 200)
		
		for x in range(self.shape[0]):
			for y in range(self.shape[1]):
				px = x*self.blockSize
				py = y*self.blockSize
				rect = pygame.Rect(px, py, self.blockSize, self.blockSize)
				pygame.draw.rect(self.screen, BLACK, rect, 1)
				
				if self.board[x][y] == 'W':
					pygame.draw.circle(self.screen, WHITE, (px,py), self.blockSize//2)
				if self.board[x][y] == 'B':
					pygame.draw.circle(self.screen, BLACK, (px,py), self.blockSize//2)
		pygame.display.update()


if __name__ == '__main__':
	game = Go(shape=(9,9), size=40)
	try:
		game.play()
	except KeyboardInterrupt:
		print('\nYou have quit the game!')
