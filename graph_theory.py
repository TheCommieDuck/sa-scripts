import sa, statistics
import networkx as nx

if __name__ == "__main__":
	assemblies = sa.load_all()
	connected_graphs = [nx.number_connected_components(ass.graph.connections) for ass in assemblies]
	print('Average number of connected assemblies:', round(sum(connected_graphs)/len(connected_graphs), 3))
	clustering_coef = [nx.average_clustering(ass.graph.neighbourhood) for ass in assemblies]
	conn_clustering_coef = [nx.average_clustering(nx.Graph(ass.graph.connections)) for ass in assemblies]
	print('Average clustering coefficient over neighbourhood graph:', round(sum(clustering_coef)/len(clustering_coef), 3))
	print('Average clustering coefficient over connections graph:', round(sum(conn_clustering_coef)/len(conn_clustering_coef), 3))
	degree_assortativity_coefficient = [nx.degree_assortativity_coefficient(ass.graph.neighbourhood) for ass in assemblies]
	conn_degree_assortativity_coefficient = [nx.degree_assortativity_coefficient(nx.Graph(ass.graph.connections)) for ass in assemblies]
	print('Average assortativity coefficient over neighbourhood graph:', round(sum(degree_assortativity_coefficient)/len(degree_assortativity_coefficient), 3))
	print('Average assortativity coefficient over connections graph:', round(sum(conn_degree_assortativity_coefficient)/len(conn_degree_assortativity_coefficient), 3))
