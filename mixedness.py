import sa, statistics
import networkx as nx
from scipy import stats
from scipy.stats import hypergeom

if __name__ == "__main__":
	assemblies = sa.load_all(True)
	prob_mix = []
	intersect_num = []
	for i in range(0, len(assemblies)-1):
		for id, pi in assemblies[i].pieces.items():
			curr_size = 6#len(pi.neighbourhood)
			next_size = 0
			intersect = 0
			try:
				next_size = 6#len(assemblies[i+1].pieces[id].neighbourhood)
				intersect = len(pi.neighbourhood.intersection(assemblies[i+1].pieces[id].neighbourhood))
				intersect_num.append(intersect)
			except KeyError:
				pass
			prob_mix.append(hypergeom.cdf(intersect, sa.num_pieces, curr_size, next_size))
	for i in range(0, 5):	
		print('Found', i, 'shared: ', sum(1 if x == i else 0 for x in intersect_num), round(100*sum(1 if x == i else 0 for x in intersect_num)/len(intersect_num), 2), \
			'%; expected: ', round(100*hypergeom.pmf(i, 100, 4, 4), 2), '%')