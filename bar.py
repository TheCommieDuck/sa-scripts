from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":
	data = [('A-A', 1356), ('A-B', 2918), ('A-C', 2569), ('A-D', 2742), ('A-E', 2979), ('B-B', 1329), ('B-C',  2700), ('B-D', 2727), ('B-E', 2623), ('C-C', 1286), ('C-D', 2658), ('C-E', 2751), ('D-D', 1377), ('D-E', 2648), ('E-E', 1337)]
	data = sorted(data, key=lambda tup: tup[1])
	fig = plt.figure()
	N = len(data)
	x = np.arange(1, N+1)
	y = [ num for (s, num) in data ]
	labels = [ s for (s, num) in data ]
	plt.bar(x, y, 1)
	plt.ylabel('Frequency')
	plt.xticks(x + 0.5, labels)
	plt.title( "Connection Type Frequency")
	plt.show()