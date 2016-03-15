import sa, statistics, random_assembly
from matplotlib import pyplot as plt
from scipy import stats
from scipy.stats import hypergeom
import sys
import math

def calc_knowledge(assemblies, decay=0.1):
	knowledge = {}
	cumul_knowledge = []
	t = 0
	#print([(c.p1, c.p2) for ass in assemblies for c in ass.connections])
	for ass in assemblies:
		if t == 74:
			t = t+1
			continue
		for piece in ass.pieces.values():
			if piece.id not in knowledge:
				knowledge[piece.id] = set()
			for known in piece.connections:
				toremove = []
				for (exist_p, epv) in knowledge[piece.id]:
					if exist_p == known.p1:
						toremove.append((exist_p, epv))
					if exist_p == known.p2:
						toremove.append((exist_p, epv))
				for i in toremove:
					knowledge[piece.id].remove(i)
				knowledge[piece.id].add((known.p1, t))
				knowledge[piece.id].add((known.p2, t))
		#print("Knowledge: " + str(sum(len(piece_knowledge)/100 for piece_knowledge in knowledge.values())))
		#print(knowledge.values())
		expval = [math.exp(-decay * (t - tup[1])) for know_set in knowledge.values() for tup in know_set]
		#print(t, max(expval))
		#for p in knowledge.values():
		#	print(len(p))
		cumul_knowledge.append(sum(expval)/100)
		t = t+1
	return (knowledge, cumul_knowledge)

def make_fig(lam, siz, exp, rand):
	#plt.figure(num)
	plt.title('avg_kd(t), Lambda='+str(lam))
	assl, = plt.plot(range(siz), exp, label="avg_kd(t) Lambda="+str(lam)) 
	randassl, = plt.plot(range(siz), rand, label="Random avg_kd(t)Lambda="+str(lam), linestyle='--')
	return [assl, randassl]

if __name__ == "__main__":
	assemblies = sa.load_all(dir=sys.argv[1])
	rand_assemblies = sa.load_all(dir='random', rand_amounts=[len(ass.connections) for ass in assemblies])

	(assem_knowledge, assem_cumul_knowledge) = calc_knowledge(assemblies, 0.5)
	(random_assem_knowledge, random_assem_cumul_knowledge) = calc_knowledge(rand_assemblies, 0.5)
	l1 = make_fig(0.5, len(assemblies)-1, assem_cumul_knowledge, random_assem_cumul_knowledge)

	#(assem_knowledge, assem_cumul_knowledge) = calc_knowledge(assemblies, 0.02)
	#(random_assem_knowledge, random_assem_cumul_knowledge) = calc_knowledge(rand_assemblies, 0.02)
	#l5 = make_fig(0.02, len(assemblies)-1, assem_cumul_knowledge, random_assem_cumul_knowledge)

	(assem_knowledge, assem_cumul_knowledge) = calc_knowledge(assemblies, 0.5)
	(random_assem_knowledge, random_assem_cumul_knowledge) = calc_knowledge(rand_assemblies, 0.5)
	l2 = make_fig(0.5, len(assemblies)-1, assem_cumul_knowledge, random_assem_cumul_knowledge)

	#(assem_knowledge, assem_cumul_knowledge) = calc_knowledge(assemblies, 0.1)
	#(random_assem_knowledge, random_assem_cumul_knowledge) = calc_knowledge(rand_assemblies, 0.1)
	#l3 = make_fig(0.1, len(assemblies)-1, assem_cumul_knowledge, random_assem_cumul_knowledge)

	(assem_knowledge, assem_cumul_knowledge) = calc_knowledge(assemblies, 0.5)
	(random_assem_knowledge, random_assem_cumul_knowledge) = calc_knowledge(rand_assemblies, 0.5)
	l4 = make_fig(0.5, len(assemblies)-1, assem_cumul_knowledge, random_assem_cumul_knowledge)
	
	plt.legend(bbox_to_anchor=(1, 0.9), handles=l1+l2+l4)
	plt.xlabel('Time')
	plt.ylabel('avg_kd(t)')
	plt.show()