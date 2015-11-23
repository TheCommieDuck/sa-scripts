import sa, statistics

if __name__ == "__main__":
	assemblies = sa.load_all()
	marker_total = []
	found_marker_total = []
	piece_total = []
	found_piece_total = []
	for assembly in assemblies:
		marker_total.append(assembly.total_markers + assembly.found_markers)
		found_marker_total.append(assembly.found_markers)
		piece_total.append(assembly.total_pieces)
		found_piece_total.append(assembly.found_pieces)
	pavg = statistics.mean(found_piece_total)/piece_total[0]
	print('Found pieces: ' + str(sum(found_piece_total)) + '/' + str(sum(piece_total)) \
		+ ' (' + str(round(pavg*100, 2)) + '%)')
	pvariance = statistics.pvariance(found_piece_total)
	print('Variance in no. found pieces: ' + str(round(pvariance, 2)))
	mavg = statistics.mean(found_marker_total)/marker_total[0]
	print('Found markers: ' + str(sum(found_marker_total)) + '/' + str(sum(marker_total)) \
		+ ' (' + str(round(mavg*100, 2)) + '%)')
	mvariance = statistics.variance(found_marker_total, mavg*marker_total[0])
	print('Variance in no. found markers: ' + str(mvariance))
	print(found_marker_total)
