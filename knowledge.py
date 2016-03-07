import sa, statistics, random_assembly
from matplotlib import pyplot as plt
from scipy import stats
from scipy.stats import hypergeom
import sys

if __name__ == "__main__":
	assemblies = sa.load_all(dir=sys.argv[1])
	knowledge = {}
	cum_knowledge = []
	for ass in assemblies:
		for piece in ass.pieces.values():
			if piece.id not in knowledge:
				knowledge[piece.id] = set()
			for known in piece.connections:
				knowledge[piece.id].add(known.p1)
				knowledge[piece.id].add(known.p2)
		print("Knowledge: " + str(sum(len(piece_knowledge)/100 for piece_knowledge in knowledge.values())))
		cum_knowledge.append(sum(len(piece_knowledge)/100 for piece_knowledge in knowledge.values()))
	plt.figure(1)
	plt.title('k(t)')
	plt.plot(range(len(assemblies)), cum_knowledge) 
	plt.show()