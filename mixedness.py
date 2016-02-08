import sa, statistics, random_assembly
import networkx as nx
from scipy import stats
from scipy.stats import hypergeom

if __name__ == "__main__":
	curr_size = 6
	#assemblies = sa.load_all(True, 	curr_size)
	assemblies = random_assembly.load_all()
	prob_mix = []
	intersect_num = []
	for i in range(0, len(assemblies)-1):
		for id, pi in assemblies[i].pieces.items():
			next_size = 6
			intersect = 0
			try:
				intersect = len(pi.neighbourhood.intersection(assemblies[i+1].pieces[id].neighbourhood))
				intersect_num.append(intersect)
			except KeyError:
				pass
			
	for i in range(0, curr_size+1):	
		print('Found', i, 'shared: ', sum(1 if x == i else 0 for x in intersect_num), round(100*sum(1 if x == i else 0 for x in intersect_num)/len(intersect_num), 2), \
			'%; expected: ', round(100*hypergeom.pmf(i, 100, curr_size, curr_size), 2), '%')