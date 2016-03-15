import sa, random

def dist(p1, p2):
	return ((p1.position[0] - p2.position[0])**2) + ((p1.position[1] - p2.position[1]) ** 2)

def make_random_assembly(amount=0):
	assembly = sa.Assembly(sa.num_pieces)
	for i in range(sa.num_pieces):
		piece = sa.Piece(i)
		x = random.randint(0, 10000)
		piece.position = (x,random.randint(0, 10000)) # random.randint(0, x))
		piece.rotation = 0
		assembly.pieces[i] = piece

	smallest = []
	clone_list = list(assembly.pieces.values())
	while len(clone_list) > 0:
		p1 = clone_list.pop(0)
		for p2 in clone_list:
			smallest.append((dist(p1, p2), p1, p2))
	smallest.sort(key=lambda t: t[0])
	for i in range(amount):
		(_, p1, p2) = smallest[i]
		assembly.add_connection(sa.Connection([p1.id, p2.id, 0, 0]))
	assembly.update_neighbourhoods(sa.k_nearest)
	return assembly

def load_all(n, amounts=[]):
	if amounts == []:
		amounts = [0 for _ in range(n)]
	return [make_random_assembly(amounts[i]) for i in range(n)]
