import sa, random

def make_random_assembly():
	assembly = sa.Assembly(sa.num_pieces)
	for i in range(sa.num_pieces):
		piece = sa.Piece(i)
		x = random.randint(0, 1000)
		piece.position = (x,random.randint(0, 1000)) # random.randint(0, x))
		piece.rotation = 0
		assembly.pieces[i] = piece
	for piece in assembly.pieces.values():

	assembly.update_neighbourhoods(sa.k_nearest)
	return assembly

def load_all(n):
	return [make_random_assembly() for i in range(n)]
