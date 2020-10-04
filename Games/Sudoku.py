board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

class SudokuSolver:
	def __init__(self, board):
		self.board = board
	
	def __repr__(self):
	    str_grid = ""
	    for i in range(len(self.board)):
	        if i % 3 == 0 and i != 0:
	            str_grid += ("- - - - - - - - - - - - \n")
	        for j in range(len(self.board[0])):
	            if j % 3 == 0 and j != 0:
	                str_grid += (" | ")
	            if j == 8:
	                str_grid += str((self.board[i][j])) + '\n'
	            else:
	                str_grid += (str(self.board[i][j]) + " ")
	    return str_grid

	def solve(self):
	    pos_found = self.find_next_empty_pos()
	    if not pos_found:
	        return True
	    else:
	        row, col = pos_found
	    for i in range(1,10):
	        if self.valid(i, (row, col)):
	            self.board[row][col] = i
	            if self.solve():
	                return True
	            self.board[row][col] = 0

	def valid(self, num, pos):
	    # Check row
	    for i in range(len(self.board[0])):
	        if self.board[pos[0]][i] == num and pos[1] != i:
	            return False
	   
	     # Check column
	    for i in range(len(self.board)):
	        if self.board[i][pos[1]] == num and pos[0] != i:
	            return False
	   
	     # Check box
	    box_x = pos[1] // 3
	    box_y = pos[0] // 3
	    for i in range(box_y*3, box_y*3 + 3):
	        for j in range(box_x * 3, box_x*3 + 3):
	            if self.board[i][j] == num and (i,j) != pos:
	                return False
	   
	     # default
	    return True

	def find_next_empty_pos(self):
	    for r in range(len(self.board)):
	        for c in range(len(self.board[0])):
	            if self.board[r][c] == 0:
	                return (r, c)  # row, column


if __name__ == "__main__":
	sudoku = SudokuSolver(board)
	sudoku.solve()
	print(sudoku)
