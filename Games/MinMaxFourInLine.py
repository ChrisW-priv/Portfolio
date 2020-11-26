import numpy as np
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


class FourInLine:
	def __init__(self, board=np.empty(shape=(7, 6), dtype=str)):
		self.board = board
		self.next = []
		self.value = 0
		self.players = ['W', 'B']
		self.current_player = self.players[self.lvl % 2]

	def __repr__(self):
		str_grid = "1   2   3   4   5   6   7\n-   -   -   -   -   -   -\n"
		for y in range(6):
			if y != 0:
				str_grid += "- - - - - - - - - - - - -\n"
			for x in range(7):
				position = self.board[x][5-y]
				if x % 1 == 0 and x != 0:
					str_grid += " | "
				if position == '':
					str_grid += ' '
				if x == 6:
					str_grid += position + '\n'
				else:
					str_grid += position
		return f"{self.lvl}\n{self.highest}\n{str_grid}"

	@property
	def is_symmetric(self):
		return np.all(self.board == self.board[::-1])

	@property
	def highest(self):
		return [6 - np.unique(v, return_counts=True)[1][0] for v in self.board]

	@property
	def lvl(self):
		return sum(self.highest)

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

	def possible_moves(self):
		moves = []
		nonsense_moves = []
		if self.is_symmetric:
			nonsense_moves = [4, 5, 6]
		if self.found_direct_win(self.current_player):
			self.value = 1
			moves.append(self.found_direct_win(self.current_player))
		else:
			for move in range(7):
				if self.highest[move] < 6 and move not in nonsense_moves \
						and not self.move_leading_to_direct_loss(move, self.current_player):
					moves.append(move)
		return moves

	def found_direct_win(self, player):
		for move, highest in enumerate(self.highest):
			if highest < 5:
				self.move(move, player)
				if self.there_is_a_winner():
					return move
				self.move_back(move)

	def move_leading_to_direct_loss(self, move, player):
		# check if opponent has a direct win if we do not prevent it
		opponent = self.players[self.players.index(player)-1]
		self.move(move, player)
		if_found = self.found_direct_win(opponent)
		self.move_back(move)
		return if_found

	def move(self, move, player):
		self.board[move][self.highest[move]] = player

	def move_back(self, move):
		self.board[move][self.highest[move]-1] = ''


class FourInLineTreeMinMaxEvaluation:
	def __init__(self, max_lvl=1, first_state=FourInLine()):
		self.first_state = first_state
		self.nodes_to_do = []

		self.MAX_LVL = max_lvl
		self.create_tree()

	def create_tree(self):
		self.expand_node(self.first_state)
		for node in self.nodes_to_do:
			self.expand_node(node)

	def expand_node(self, node):
		def create_new_node(move):
			new_state = FourInLine( deepcopy(node.board) )
			new_state.move(move, new_state.current_player)
			node.next.append(new_state)
			return new_state

		def create_new_nodes(top_node):
			with ThreadPoolExecutor() as executor:
				return executor.map(create_new_node, top_node.possible_moves())

		if node.lvl < self.MAX_LVL:
			for new_node in create_new_nodes(node):
				self.nodes_to_do.append(new_node)

	def print_positions(self, game_state=None, all_=False):
		if not game_state:
			game_state = self.first_state
		if not all_:
			if not game_state.next:
				print(game_state)
			else:
				for next_tile in game_state.next:
					self.print_positions(next_tile)
		else:
			print(game_state)
			for next_state in game_state.next:
				self.print_positions(next_state)


if __name__ == "__main__":
	DEPTH = 3

	tree_search = FourInLineTreeMinMaxEvaluation(DEPTH)
	tree_search.print_positions(all_=True)
