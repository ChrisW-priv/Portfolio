class Sudoku:
	def __init__(self, matrix):
		self.matrix = matrix
		self.solve()

	def solve(self):
		for y in range(9):
			for x in range(9):
				if self.matrix[y][x] == 0:
					for n in range(1,10):
						if self.possible(y,x,n):
							self.matrix[y][x] = n
							self.solve()
							self.matrix[y][x] = 0
					return
		print(self.matrix)

	def possible(self, y,x,n):
		for i in range(9):
			if self.matrix[y][i] == n:
				return False
		for i in range(9):
			if self.matrix[i][x] == n:
				return False

		x0 = (x//3)*3
		y0 = (x//3)*3

		for i in range(3):
			for j in range(3):
				if self.matrix[y0+1][x0+j] == n:
					return False




matrix = [
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
]

sudoku = Sudoku(matrix)
sudoku.solve()
print(sudoku.matrix)