
class Tile:
	def __init__(self, value):
		self.seen = False
		self.flaged=False
		self.value = str(value)
	def __repr__(self):
		if self.value == '0':
			return ' '
		else:
			return self.value[0]


class BoardBuilder:
	def __init__(self, shape=(10,10), n_mines=10):
		import numpy as np
		
		self.n_mines = n_mines
		self.shape = shape
		self.matrix = np.ndarray(shape=shape, dtype=Tile)
		self.create_bombs()
		self.fill_matrix_with_nums()

	def __repr__(self):
		s = ''
		for row in self.matrix:
			for i, value in enumerate(row):
				s += str(value)
				s += ' '
				if i == self.shape[0]-1:
					s+='\n'
		return s

	def create_bombs(self):
		import random as rd
		
		for i in range(self.n_mines):
			while True:
				x = rd.randrange(self.shape[0])
				y = rd.randrange(self.shape[1])
				if type(self.matrix[x][y]) != Tile:
					self.matrix[x][y] = Tile('BOMB')
					# print('Bomb created at pos (X,Y):',x,y)
					break

	def fill_matrix_with_nums(self):
		for y in range(self.shape[1]):
			for x in range(self.shape[0]):
				pos = self.matrix[x][y]
				if type(pos) != Tile:
					n_mines = self.count_bombs_around(pos=(x,y))
					self.matrix[x][y]=Tile(n_mines)

	def count_bombs_around(self, pos):
		bombs_count=0
		x,y = pos
		to_check = [ (-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1) ]
		for check in to_check:
			try:
				cx,cy = check
				if y+cy<0 or x+cx<0:
					continue
				tile = (self.matrix)[ x+cx ][ y+cy ]
				if tile.value == 'BOMB':
					bombs_count+=1
			except IndexError:
				continue
			except AttributeError:
				continue
		return bombs_count


if __name__ == '__main__':
	board = BoardBuilder()
	print(board)
