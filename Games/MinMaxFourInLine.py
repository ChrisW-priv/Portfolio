import numpy as np
from copy import deepcopy


class FourInLine:
	def __init__(self, board=np.empty(shape=(6,7), dtype=str)):
		self.board = board
		self.highest = [0,0,0,0,0,0,0]
		self.lvl = 0
		self.next = []
		self.value = 0

	def __repr__(self):
		str_grid = "1   2   3   4   5   6   7 \n-   -   -   -   -   -   -\n"
		for i in range(len(self.board)):
			if i % 1 == 0 and i != 0:
				str_grid += ("- - - - - - - - - - - - -\n")
			for j in range(len(self.board[0])):
				if j % 1 == 0 and j != 0:
					str_grid += (" | ")
				if self.board[i][j] == '':
					str_grid += ' '
				if j == 6:
					str_grid += str((self.board[i][j])) + '\n'
				else:
					str_grid += (str(self.board[i][j]) + "")
		return str_grid

	def move(self, move, player):
		x = self.board.shape[0]-self.highest[move]-1
		self.board[x][move] = player
		self.highest[move] += 1
		
	def there_is_a_winner(self):
		if sum(self.highest)>=7:
			b = self.board # makes writing code bit more easies
			horizontal_line = lambda row, column: \
				True if (b[row][column]==b[row][column+1]==b[row][column+2]==b[row][column+3]!='') else False
			vertical_line = lambda row, column: \
				True if (b[row][column]==b[row+1][column]==b[row+2][column]==b[row+3][column]!='') else False
			diagonal_right_line = lambda row, column: \
				True if (b[row][column]==b[row+1][column+1]==b[row+2][column+2]==b[row+3][column+3]!='') else False
			diagonal_left_line = lambda row, column: \
				True if (b[row][column]==b[row+1][column-1]==b[row+2][column-2]==b[row+3][column-3]!='') else False

			horizontal_lines = [horizontal_line(row,col) for row in range(6) for col in range(4)]
			vertical_lines = [vertical_line(row,col) for row in range(3) for col in range(7)]
			diagonal_right_lines = [diagonal_right_line(row,col) for row in range(3) for col in range(4)]
			diagonal_left_lines = [diagonal_left_line(row,col) for row in range(3) for col in range(4,7)]

			return True in horizontal_lines+vertical_lines+diagonal_right_lines+diagonal_left_lines


class FourInLineTreeMinMaxEvaluation:
	def __init__(self, max_lvl=1, first_state=FourInLine()):
		self.first_state = first_state
		self.tiles_to_do = [first_state]
		
		self.PLAYERS = {0: 'W', 1: 'B'}
		self.MAX_LVL = max_lvl
		self.create_tree()
		self.update_node_values()

	def create_tree(self):
		while self.tiles_to_do:
			top = self.tiles_to_do.pop(0)
			current_lvl = top.lvl+1
			for column, height in enumerate(top.highest):
				if height == 6:
					continue
				else:
					new_state = deepcopy(top)
					new_state.next = []
					new_state.lvl = current_lvl
					current_player = self.PLAYERS[current_lvl%2]
					new_state.move(column, current_player)
					if new_state.there_is_a_winner():
						if current_player == 'W':
							new_state.value = 1
						if current_player == 'B':
							new_state.value = -1
					top.next.append(new_state)
					if current_lvl < self.MAX_LVL:
						self.tiles_to_do.append(new_state)

	def update_node_values(self):
		for _ in range(self.MAX_LVL):
			self.go_down(self.first_state)

	# update values from bottom to top
	def go_down(self, game_state):
		values_next = [game_state.value for game_state in game_state.next]
		if game_state.value == 0 and None not in values_next:
			if game_state.lvl%2==0:
				game_state.value = max(values_next)
			else:
				game_state.value = min(values_next)
		else:
			for next_game_state in game_state.next:
				self.go_down(next_game_state)

	def print_all_positions(self, game_state=None):
		if not game_state:
			game_state = self.first_state
		print(game_state)
		# print(game_state.lvl, game_state, sep='\n')
		for next_state in game_state.next:
			self.print_all_positions(next_state)

	def board_on_the_bottom(self, game_state=None):
		if not game_state:
			game_state = self.first_state
		if not game_state.next:
			print( game_state )
		else:
			for next_tile in game_state.next:
				self.board_on_the_bottom(next_tile)


if __name__ == "__main__":
	import sys
	DEPTH = 12
	sys.setrecursionlimit( min( 10000, 7**DEPTH ) )

	tree_search = FourInLineTreeMinMaxEvaluation(DEPTH)
	# tree_search.print_all_positions()
	# tree_search.board_on_the_bottom()
	print(tree_search.first_state.value)
