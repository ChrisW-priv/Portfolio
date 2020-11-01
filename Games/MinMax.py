import random as rd

class Tile():
	def __init__(self, lvl=0, value=None):
		self.lvl = lvl
		self.value = value
		self.next = []

tile_1 = Tile()
tiles_to_do = [tile_1]

MAX_LVL = 3
BRANCHES = 2
values_on_the_end = list( range(1, BRANCHES**MAX_LVL+1) );i=0
rd.shuffle(values_on_the_end)

# create tree
current_lvl = 0
while tiles_to_do:
	top = tiles_to_do.pop(0)
	current_lvl = top.lvl+1
	for _ in range(BRANCHES):
		if current_lvl == MAX_LVL:
			new_tile = Tile(current_lvl, values_on_the_end[i])
			top.next.append(new_tile)
			i+=1
		else:
			new_tile = Tile(current_lvl)
			top.next.append(new_tile)
			tiles_to_do.append(new_tile)

# print values on the bottom
def go_down(tile):
	if tile.value != None:
		print(tile.value, end=' ')
	else:
		for next_tile in tile.next:
			go_down(next_tile)

go_down(tile_1)
