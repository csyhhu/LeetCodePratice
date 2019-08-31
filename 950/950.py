from queue import Queue

def deckRevealedIncreasing(deck):
	
	n = len(deck)
	order = list() # Index represent placement, value for real order
	q = Queue()
	for i in range(n):
		q.put(i)

	# Perform Simulation and Record the corresponding
	while True:
		order.append(q.get())
		if q.empty():
			break
		q.put(q.get())

	# Sort input array
	sorted_value = sorted(deck)
	reorder_deck = list()
	for idx in range(n):
		reorder_deck.append(sorted_value[order.index(idx)])

	return reorder_deck

deck = [17,13,11,2,3,5,7]
outputs = deckRevealedIncreasing(deck)
print(outputs)