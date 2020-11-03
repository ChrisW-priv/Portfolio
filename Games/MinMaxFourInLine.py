import numpy as np
from copy import deepcopy
import concurrent.futures


class FourInLine:
	def __init__(self, board=np.empty(shape=(7, 6), dtype=str)):
		self.board = board
		self.highest = [0, 0, 0, 0, 0, 0, 0]
		self.last_move = (0, 0)
		self.next = []
		self.value = 0
		self.lvl = 0

	def __repr__(self):
		str_grid = "1   2   3   4   5   6   7 \n-   -   -   -   -   -   -\n"
		for y in range(6):
			if y % 1 == 0 and y != 0:
				str_grid += ("- - - - - - - - - - - - -\n")
			for x in range(7):
				if x % 1 == 0 and x != 0:
					str_grid += (" | ")
				if self.board[x][y] == '':
					str_grid += ' '
				if x == 6:
					str_grid += str((self.board[x][y])) + '\n'
				else:
					str_grid += (str(self.board[x][y]) + "")
		return str_grid

	def there_is_a_winner(self):
		if sum(self.highest) >= 7:
			b = self.board  # makes writing code bit more easies
			# horizontal_line
			horizontal_line = lambda row, column: \
				True if (b[row][column] == b[row][column + 1] == b[row][column + 2] == b[row][
					column + 3] != '') else False
			# vertical_line
			vertical_line = lambda row, column: \
				True if (b[row][column] == b[row + 1][column] == b[row + 2][column] == b[row + 3][
					column] != '') else False
			# diagonal_line
			diagonal_right_line = lambda row, column: \
				True if (b[row][column] == b[row + 1][column + 1] == b[row + 2][column + 2] == b[row + 3][
					column + 3] != '') else False
			# diagonal_line
			diagonal_left_line = lambda row, column: \
				True if (b[row][column] == b[row + 1][column - 1] == b[row + 2][column - 2] == b[row + 3][
					column - 3] != '') else False

			horizontal_lines = [horizontal_line(row, col) for row in range(7) for col in range(3)]
			vertical_lines = [vertical_line(row, col) for row in range(4) for col in range(6)]
			diagonal_right_lines = [diagonal_right_line(row, col) for row in range(4) for col in range(3)]
			diagonal_left_lines = [diagonal_left_line(row, col) for row in range(4) for col in range(3, 6)]

			return True in horizontal_lines + vertical_lines + diagonal_right_lines + diagonal_left_lines

	def possible_moves(self, player):
		moves = []
		if self.find_direct_win(player):
			self.value = 1
			moves.append(self.find_direct_win(player))
		else:
			for i, highest in enumerate(self.highest):
				if highest != 6 and i not in self.move_leading_to_direct_loss(player):
					moves.append(i)
		return moves

	def find_direct_win(self, player):
		for i, highest in enumerate(self.highest):
			if highest != 6:
				self.move(i, player)
				if self.there_is_a_winner():
					return i
				else:
					self.move_back()

	def move_leading_to_direct_loss(self, player):
		# check if oponent has a direct win if we do not prevent it
		return []

	def move(self, move, player):
		y = self.board.shape[1] - self.highest[move] - 1
		self.board[move][y] = player
		self.highest[move] += 1
		self.last_move = (move, y)

	def move_back(self):
		x, y = self.last_move
		self.board[x][y] = ''
		self.highest[x] -= 1


class FourInLineTreeMinMaxEvaluation:
	def __init__(self, max_lvl=1, first_state=FourInLine()):
		self.first_state = first_state
		self.nodes_to_do = [first_state]

		self.PLAYERS = {0: 'W', 1: 'B'}
		self.MAX_LVL = max_lvl
		self.create_tree()
		for _ in range(self.MAX_LVL):
			self.go_down(self.first_state)

	def create_tree(self):
		for node in self.nodes_to_do:
			self.expand_node(node)

	def expand_node(self, node):
		current_lvl = node.lvl + 1
		current_player = self.PLAYERS[current_lvl % 2]

		def create_new_node(top_node, move):
			new_state = deepcopy(top_node)
			new_state.next = []
			new_state.lvl = current_lvl
			new_state.move(move, current_player)
			top_node.next.append(new_state)
			return new_state

		def create_new_nodes(top_node):
			with concurrent.futures.ThreadPoolExecutor() as executor:
				results = [executor.submit(create_new_node, top_node, move)
							for move in top_node.possible_moves(current_player)]
			return [result.result() for result in concurrent.futures.as_completed(results)]

		def add_nodes_to_tiles_to_do_list(nodes):
			values = [node.value for node in nodes]
			if 1 not in values and -1 not in values and current_lvl < self.MAX_LVL:
				for node in nodes:
					self.nodes_to_do.append(node)

		nodes = create_new_nodes(node)
		add_nodes_to_tiles_to_do_list(nodes)

	# update values from bottom to top
	def go_down(self, game_state):
		values_next = [game_state.value for game_state in game_state.next]
		if game_state.value == 0 and None not in values_next:
			if game_state.lvl % 2 == 0:
				game_state.value = max(values_next)
			else:
				game_state.value = min(values_next)
		else:
			for next_game_state in game_state.next:
				self.go_down(next_game_state)

	def print_all_positions(self, game_state=None):
		if not game_state:
			game_state = self.first_state
		print(game_state.lvl)
		print(game_state)
		for next_state in game_state.next:
			self.print_all_positions(next_state)

	def board_on_the_bottom(self, game_state=None):
		if not game_state:
			game_state = self.first_state
		if not game_state.next:
			print(game_state)
		else:
			for next_tile in game_state.next:
				self.board_on_the_bottom(next_tile)


if __name__ == "__main__":
	import sys

	DEPTH = 3
	sys.setrecursionlimit(min(10000, 7 ** DEPTH))

	tree_search = FourInLineTreeMinMaxEvaluation(DEPTH)
	# tree_search.print_all_positions()
	tree_search.board_on_the_bottom()
