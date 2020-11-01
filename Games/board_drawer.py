import pygame

class BoardDrawer:
	def __init__(self, game):
		if type(game) == Go:
			self.draw_GO()

	def init_board(self):
		# colours
		GRAY = (100,100,100)
		self.BLACK = (0, 0, 0)
		self.WHITE = (200, 200, 200)

		# pygame board init
		pygame.init()
		pygame.display.set_caption('GO')
		self.screen = pygame.display.set_mode( (self.shape[0]*self.blockSize, self.shape[1]*self.blockSize) )
		self.screen.fill(GRAY)
		
		# draw grid of lines
		for x in range(self.shape[0]+1):
			for y in range(self.shape[1]+1):
				px = x*self.blockSize-(self.blockSize//2)
				py = y*self.blockSize-(self.blockSize//2)
				rect = pygame.Rect(px, py, self.blockSize, self.blockSize)
				pygame.draw.rect(self.screen, self.BLACK, rect, 1)
		pygame.display.update()

	def drawGO(self):
		pass