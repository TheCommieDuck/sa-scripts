import sa, statistics
import networkx as nx

if __name__ == "__main__":
	assemblies = sa.load_all()
	clustering_coef = [nx.average_clustering(ass.graph.neighbourhood) for ass in assemblies]
	conn_clustering_coef = [nx.average_clustering(nx.Graph(ass.graph.connections)) for ass in assemblies]
	print('Average clustering coefficient over neighbourhood graph:', round(sum(clustering_coef)/len(clustering_coef), 3))
	print('Average clustering coefficient over connections graph:', round(sum(conn_clustering_coef)/len(conn_clustering_coef), 3))