import sa, random

def make_random_assembly():
	assembly = sa.Assembly(sa.num_pieces)
	for i in range(sa.num_pieces):
		piece = sa.Piece(i)
		x = random.randint(0, 1000)
		piece.position = (x, random.randint(0, 1000))
		piece.rotation = 0
		assembly.pieces[i] = piece
	assembly.update_neighbourhoods(True, sa.k_nearest)
	return assembly

def load_all():
	return [make_random_assembly() for i in range(100)]
