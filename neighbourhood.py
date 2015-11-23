import sa, statistics

if __name__ == "__main__":
	assemblies = sa.load_all()
	neighbourhood_freq = [len(piece.neighbourhood) for ass in assemblies for _, piece in ass.pieces.items()]
	print('Average neighbourhood size per piece per mix:', sum(neighbourhood_freq)/len(neighbourhood_freq))
	pvariance = statistics.pvariance(neighbourhood_freq)
	print('Variance in neighbourhood size: ' + str(round(pvariance, 2)))