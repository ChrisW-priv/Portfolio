import numpy as np
import pygame


class Tile:
	def __init__(self, player='', pos=(0,0)):
		self.player = player
		self.pos = pos
	def __repr__(self):
		return self.player


class String:
	def __init__(self, board, pos, colour):
		self.board = board
		self.tiles = [pos]
		self.colour = colour
		self.pos = pos
		self.around = []
		self.get_all_pieces(pos)
		
	def get_all_pieces(self, pos):
		pos_around = [ (0,1), (1,0), (0,-1), (-1,0) ] 
		for position in pos_around:
			nx = pos[0]+position[0]
			ny = pos[1]+position[1]
			try:
				assert nx in range(0, self.board.shape[0]) and ny in range(self.board.shape[1])
				assert (nx,ny) not in self.tiles
				player = self.board[nx][ny].player
			except AttributeError:
				continue
			except AssertionError:
				continue
			else:
				if player == self.colour:
					self.tiles.append( (nx,ny) )
					self.get_all_pieces( (nx,ny) )

	def get_surrounding_positions(self, pos):
		pos_around = [ (0,1), (1,0), (0,-1), (-1,0) ] 
		for around in pos_around:
			nx = pos[0]+around[0]
			ny = pos[1]+around[1]
			try:
				assert nx in range(0, self.board.shape[0]) and ny in range(self.board.shape[1])
				player = self.board[nx][ny].player
			except AssertionError:
				continue
			except AttributeError:
				self.around.append( self.board[nx][ny] )
			else:
				if player != self.colour:
					self.around.append( self.board[nx][ny] )

	def is_surrounded(self):
		for pos in self.tiles:
			self.get_surrounding_positions(pos)

		if None not in self.around:
			return [pos.player for pos in self.around].count(self.colour)==0


class Go:
	def __init__(self, shape=(19,19), blockSize=40):
		self.board = np.empty(shape=shape, dtype=Tile)
		self.shape = shape
		self.blockSize = blockSize
		self.moves_back = []
		self.moves_forward = []
		self.white_prisoners = 0
		self.black_prisoners = 0

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

	def drawGrid(self):		
		# for each position check if not empty and draw circle on the board
		for x in range(self.shape[0]):
			for y in range(self.shape[1]):
				try:
					block = self.board[x][y].player
				except AttributeError:
					continue
				else:
					px = x*self.blockSize
					py = y*self.blockSize
					if block == 'W':
						pygame.draw.circle(self.screen, self.WHITE, (px+self.blockSize//2,py+self.blockSize//2), self.blockSize//2)
					if block == 'B':
						pygame.draw.circle(self.screen, self.BLACK, (px+self.blockSize//2,py+self.blockSize//2), self.blockSize//2)
		pygame.display.update()

	def quit(self):
		from sys import exit
		pygame.quit(); exit()
		
	def play(self):
		self.init_board()

		self.passed = 0
		# play until finished
		while True:
			for player in ['B','W']:
				move_ok=False
				while not move_ok:
					for event in pygame.event.get():
						# if clicks close
						if event.type == pygame.QUIT:
							self.quit()
						
						# each mouse click will be couted as a move
						elif event.type == pygame.MOUSEBUTTONDOWN:
							# get position of mouse and devide it by blocksize to match self.size constrains
							move = pygame.mouse.get_pos()
							x = move[0]//self.blockSize
							y = move[1]//self.blockSize
							move_ok = self.move( (x,y), player )
							if move_ok:
								self.drawGrid()
								self.passed=0
								self.moves_forward=[]
						
						# if makes mistake use keyboard to move undo last move
						elif event.type == pygame.KEYDOWN:
							# pass
							if event.key == pygame.K_p:
								self.passed+=1
								move_ok=True
							# move back
							if event.key == pygame.K_b:
								self.move_back()
								move_ok=True
							if event.key == pygame.K_f:
								self.move_forward()
								move_ok=True
								
				if self.game_is_finished():
					winner = self.decide_winner()
					self.win_screen(winner)

	def move(self, move, player):
		def move_is_suicidal(x,y):
			# jeżeli w tym ruchu powstaje string o kolorze obecnego gracza i nie powstaje żaden string gracza przeciwnego
			self.board[x][y] = Tile(player, (x,y))
			colours_of_strings = [string.colour for string in self.all_strings() if string.is_surrounded()]
			self.board[x][y] = None
			return len(colours_of_strings)>0 and len(colours_of_strings)==colours_of_strings.count(player)

		def move_is_ok_with_KO_rule(x,y):
			# if move does not lead to recapture of same tile (captured in last move)
			from copy import copy
			
			def matrix_equal(m1,m2):
				ax,ay = np.where( m1 != m2 )
				for x,y in zip( ax,ay ):
					try:
						a = m1[x][y].player
						b = m2[x][y].player
					except AttributeError:
						a = m1[x][y]
						b = m2[x][y]
					finally:
						if a==b:
							continue
						else:
							return False
				return True

			if len(self.moves_back)>1:
				self.move_back()
				state_one_move_before = copy(self.board)
				self.move_forward()
				self.palce_stone((x,y), player)
				if not matrix_equal(state_one_move_before, self.board):
					return True
				else:
					self.move_back()
			else:
				self.palce_stone((x,y), player)
				return True

		try:
			# check if move is valid
			x,y = move
			if self.board[x][y] != None:
				raise MoveNotValidError('This position is already taken')
			if move_is_suicidal(x,y):
				raise MoveNotValidError('This move is suicidal')
			if not move_is_ok_with_KO_rule(x,y):
				raise MoveNotValidError('This move is against the KO rule')
		except MoveNotValidError as e:
			print('Move not valid!', e)
			return False
		else:
			return True

	def palce_stone(self, move, player):
		x,y = move
		# update board
		self.board[x][y] = Tile(player, move)
		# update moves log
		self.moves_back.append( Tile(player, move) )
		# check if there has been any captures
		for string in self.all_strings():
			if string.colour!=player and string.is_surrounded():
				self.update_prisoners(string.colour, len(string.tiles))
				self.remove_string(string)
				self.init_board()

	def move_back(self):
		try:
			last = self.moves_back.pop(-1)
		except IndexError:
			print('There are no moves played before this position!')
		else:
			if type(last) == String:
				for pos in last.tiles:
					x,y = pos
					self.board[x][y] = Tile(last.colour, pos)
				self.move_back()
			if type(last) == Tile:
				# clear last added piece
				self.moves_forward.append(last)
				lx,ly=last.pos
				self.board[lx][ly]=None
			self.init_board()
			self.drawGrid()

	def move_forward(self):
		try:
			last = self.moves_forward.pop(-1)
		except IndexError:
			print('There are no moves played after this position!')
		else:
			self.palce_stone(last.pos, last.player)

			self.init_board()
			self.drawGrid()

	def all_strings(self):
		all_strings=[]
		for x in range(self.shape[0]):
			for y in range(self.shape[1]):
				pos = (x,y)
				if self.board[x][y] != None:
					if pos not in [position_seen for string in all_strings for position_seen in string.tiles]:
						string=String(self.board, pos, self.board[x][y].player)
						all_strings.append(string)
				else:
					string = String(self.board, pos, None)
		return all_strings

	def remove_string(self, string):
		self.moves_back.append(string)
		for pos in string.tiles:
			x,y = pos
			self.board[x][y] = None

	def drawing_mode(self):
		self.init_board()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					# get position of mouse and devide it by blocksize to match self.size constrains
					move = pygame.mouse.get_pos()
					x = move[0]//self.blockSize
					y = move[1]//self.blockSize
					pl={1:'B', 3:"W"}
					if event.button in [1, 3]:
						self.palce_stone( (x,y), pl[event.button])
						self.moves_forward=[]
						# finally display changes
						self.drawGrid()
				elif event.type == pygame.KEYDOWN:
					# move back
					if event.key == pygame.K_b:
						self.move_back()
					if event.key == pygame.K_f:
						self.move_forward()

	def update_prisoners(self, player, prisoners_count):
		teritories = {'W':0,'B':0}
		teritories[player] = prisoners_count

		self.white_prisoners += teritories['B']
		self.black_prisoners += teritories['W']

	def game_is_finished(self):
		if self.passed >= 2:
			return True
		for x in range(self.shape[0]):
			for y in range(self.shape[1]):
				if self.board[x][y] == None:
					return False
		return True

	def decide_winner(self):
		teritories = {'W':0,'B':0}
		for x in range(self.shape[0]):
			for y in range(self.shape[1]):
				try:
					player = self.board[x][y].player
				except AttributeError:
					continue
				else:
					teritories[player] += 1
		for string in self.all_strings():
			if string.colour==None and string.is_surrounded():
				teritories[string.around[0].player] += 1

		self.white_score = self.white_prisoners + teritories['W'];print(self.white_score)
		self.black_score = self.black_prisoners + teritories['B'];print(self.black_score)

		# return results
		if self.white_score > self.black_score:
			return 'White'
		elif self.white_score == self.black_score:
			return 'Draw'
		else:
			return 'Black'

	def win_screen(self, winner):
		print(f'\nPlayer "{winner}" wins!')
		pygame.init()
		font = pygame.font.SysFont('Arial', 18)
		pygame.display.set_caption('Victory!')
		screen = pygame.display.set_mode( (self.shape[0]*self.blockSize, self.shape[1]*self.blockSize) )
		screen.fill(self.WHITE)
		if winner == 'Draw':
			screen.blit(font.render('It is a draw!', False, self.BLACK), (10, 10))
		else:
			screen.blit(font.render(f'{winner} wins!', False, self.BLACK), (10, 10))
		pygame.display.update()


class MoveNotValidError(Exception):
	def __init__(self, msg):
		self.message = msg


if __name__ == '__main__':
	game = Go(shape=(9,9), blockSize=40)
	try:
		game.play()
	except KeyboardInterrupt:
		print('\nYou have quit the game!')
