class Tile:
	def __init__(self):
		self.value = None
		self.lvl = 0
		self.next = []


class MinMaxTree:
	def __init__(self, first_tile = Tile()):
		self.first_tile = first_tile
		self.tiles_to_do = [first_tile]

		self.MAX_LVL = 4
		self.BRANCHES = 4
		self.values_on_the_end = ( range(1, self.BRANCHES**self.MAX_LVL+1) ); self.i=0
		self.create_tree()
		self.go_down()

	def create_tree(self):
		while self.tiles_to_do:
			top = self.tiles_to_do.pop(0)
			current_lvl = top.lvl+1
			for _ in range(self.BRANCHES):
				new_tile = Tile()
				new_tile.lvl = current_lvl
				top.next.append(new_tile)
				if current_lvl == self.MAX_LVL:
					new_tile.value = self.values_on_the_end[self.i]; self.i+=1
				if current_lvl<self.MAX_LVL:
					self.tiles_to_do.append(new_tile)

	def go_down(self):
		for _ in range(self.MAX_LVL):
			self.update_from_the_bottom(self.first_tile)

	def update_from_the_bottom(self, tile):
		values_next = [tile.value for tile in tile.next]
		if not tile.value and None not in values_next:
			if tile.lvl%2==0:
				tile.value = max(values_next)
			else:
				tile.value = min(values_next)
		else:
			for next_tile in tile.next:
				self.update_from_the_bottom(next_tile)

	def values_on_the_bottom(self, tile=None):
		if not tile:
			tile = self.first_tile
		if tile.value:
			return tile.value
		else:
			for next_tile in tile.next:
				self.values_on_the_bottom(next_tile)


if __name__ == "__main__":
	tree = MinMaxTree()
	# print value for perfect game
	print(tree.values_on_the_bottom())
