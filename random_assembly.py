import sa, random

def make_random_assembly():
	assembly = sa.Assembly(sa.num_pieces)
	for i in range(sa.num_pieces):
		piece = sa.Piece(i)
		x = random.randint(0, 10000)
		piece.position = (x, random.randint(0, x))
		piece.rotation = 0
		assembly.pieces[i] = piece
	assembly.update_neighbourhoods(sa.k_nearest)
	return assembly

def load_all(n):
	return [make_random_assembly() for i in range(n)]
