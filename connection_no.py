import sa

if __name__ == "__main__":
	assemblies = sa.load_all()
	connection_freq = {(x, y): 0 for x in range(0, sa.total_binding_sites) for y in range(0, sa.total_binding_sites) if x <= y}
	total_conns = 0
	for ass in assemblies:
		for conn in ass.connections:
			c1 = min(conn.c1, conn.c2)
			c2 = max(conn.c1, conn.c2)
			connection_freq[(c1, c2)] = connection_freq[(c1, c2)] + 1
			total_conns += 1
	print('Connection type:')
	d = connection_freq
	for c1, c2 in sorted(d, key=lambda i: -int(d[i])):
		print(c1, '-', c2, ": %d (%5.2f%%)" % (connection_freq[(c1, c2)], connection_freq[(c1, c2)]*100/total_conns))
	print('Total connections:', total_conns)
	print('Average connections per mix:', int(total_conns/sa.num_mixes))
	print('Average connections per piece per mix:', round(total_conns/14976, 2))
	most = max(connection_freq.items(), key=lambda x: x[1])
	print('Most common connection: ', most, '%.2f%%' % (most[1]*100/total_conns))
	least = min(connection_freq.items(), key=lambda x: x[1])
	print('Most uncommon connection: ', least, '%.2f%%' %  (least[1]*100/total_conns))