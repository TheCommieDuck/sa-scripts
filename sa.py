import csv, os, math, matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial import KDTree
import numpy as np
import random_assembly
import sys
num_pieces = 100
total_binding_sites = 10
num_mixes = 0
k_nearest = 6

def get_parent_dir(directory):
    return os.path.dirname(directory)

def load_all(dir="output", k=6, rand_nums=150, rand_amounts=[]):
	if dir == 'random':
		assemblies = random_assembly.load_all(rand_nums, rand_amounts)
	else:
		path = os.path.join(get_parent_dir(os.getcwd()), dir)
		files = [ os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
		assemblies = [load_stats(file, k) for file in files]
		global num_mixes
		num_mixes = len(assemblies)
	return assemblies

def load_stats(file, k=6):
	assembly = Assembly(num_pieces) #todo: read this from file
	with open(file, 'r') as csvfile:
		reader = csv.reader(csvfile)
		markers = next(reader)
		assembly.found_markers = int(markers[0])
		assembly.total_markers = int(markers[1])
		pieces = next(reader)
		assembly.found_pieces = int(pieces[0])
		assembly.total_pieces = int(pieces[1])
		assembly.connections = []
		assembly.pieces = {}
		assembly.set_radius(float(next(reader)[0])/2)
		reached_connections = False
		for line in reader:
			if line[0] == 'connections':
				reached_connections = True
				continue
			if reached_connections:
				assembly.add_connection(Connection(line))
			else:
				split_line = line
				id = int(split_line[0])
				piece = Piece(id)
				piece.position = (float(split_line[1]), float(split_line[2]))
				piece.rotation = float(split_line[3])
				for i in range(4,len(split_line),2):
  					piece.connection_locations.append((float(split_line[i]), float(split_line[i+1])))
				assembly.pieces[id] = piece
		assembly.update_neighbourhoods(k)
	return assembly

def distance(d1, d2):
	return math.sqrt((d1[0] -d2[0])**2 + (d1[1] -d2[1])**2)

class Assembly:
	def __init__(self, total_pieces):
		self.connections = []
		self.pieces = {x:Piece(x) for x in range(0, total_pieces)}
		self.graph = AssemblyGraph(total_pieces)
	
	def set_radius(self, rad):
		self.radius = rad
		self.neighbourhood_dist = (rad/2)+24

	def update_neighbourhoods(self, k1):
		tree = KDTree([piece.position for _, piece in self.pieces.items()])
		for p1 in range(0, num_pieces):
			try:
				nearest = tree.query(self.pieces[p1].position, k=k1+1)
				for n in nearest[1]:
					if n == p1:
						continue
					if len(self.pieces[p1].neighbourhood) >= k1: #if we've added them, stop
						break
					self.pieces[p1].neighbourhood.add(n)
					self.graph.add_neighbourhood(p1, n, distance(self.pieces[p1].position, self.pieces[n].position))
			except KeyError:
					pass

	def add_connection(self, connection):
		p1 = connection.p1
		p2 = connection.p2
		if p1 not in self.pieces:
			self.pieces[p1] = Piece(p1)
		if p2 not in self.pieces:
			self.pieces[p2] = Piece(p2)
		self.pieces[p1].connections.add(connection)
		self.pieces[p2].connections.add(connection)
		self.connections.append(connection)
		self.graph.add_connection(p1, p2, connection)

	def get_neighbourhood(self, piece_id):
		return self.pieces[piece_id].neighbourhood

class Connection:
	def __init__(self, data):
		self.p1 = int(data[0])
		self.p2 = int(data[1])
		self.c1 = int(data[2])
		self.c2 = int(data[3])

	def __hash__(self):
		return (31 * self.p1) ^ (31 * self.p2) ^ (13 * self.c1) ^ (31 * self.c2)

class Piece:
	def __init__(self, id):
		self.id = id
		self.neighbourhood = set()
		self.connections = set()
		self.position = None
		self.connection_locations = []

class AssemblyGraph:
	def __init__(self, node_count):
		self.connections = nx.MultiGraph() #nx.empty_graph(node_count, nx.MultiGraph()) 
		self.neighbourhood = nx.Graph() #nx.empty_graph(node_count)

	def add_neighbourhood(self, n1, n2, dist):
		self.neighbourhood.add_edge(n1, n2, distance=dist)

	def add_connection(self, n1, n2, conn):
		self.connections.add_edge(n1, n2, connection=conn)

if __name__ == "__main__":
	ass = load_all(True)
	poss = {}
	for id, piece in ass[0].pieces.items():
		poss[id] = (piece.position[0]/100, -piece.position[1]/100)
	plt.figure(1)
	plt.title('Neighbourhood Graph (k=6)')
	nx.draw_networkx(ass[0].graph.neighbourhood, pos=poss, with_labels=False)
	plt.figure(2)
	plt.title('Connections Graph')
	nx.draw_networkx(ass[0].graph.connections, pos=poss, nodelist=ass[0].graph.neighbourhood.nodes(), with_labels=False)
	plt.show()
