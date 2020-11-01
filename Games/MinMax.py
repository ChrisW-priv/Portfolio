class Tile():
	def __init__(self, lvl=0, value=None):
		self.lvl = lvl
		self.value = value
		self.next = []


first_tile = Tile()
tiles_to_do = [first_tile]

MAX_LVL = 2
BRANCHES = 3
values_on_the_end = ( range(1, BRANCHES**MAX_LVL+1) )
i=0

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

# update values from bottop to top
def go_down(tile):
	values_next = [tile.value for tile in tile.next]
	if tile.value == None and None not in values_next:
		if tile.lvl%2==0:
			tile.value = max(values_next)
		else:
			tile.value = min(values_next)
	else:
		for next_tile in tile.next:
			go_down(next_tile)

# update tree state until it reaches the top
while first_tile.value == None: 
	go_down(first_tile)

# print value for perfect game
print(first_tile.value)
