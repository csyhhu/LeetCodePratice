from queue import Queue

def deckRevealedIncreasing(self, deck):
	
	n = len(deck)
	q = Queue.Queue()
	for i in range(n):
		q.put(i)
	# Simulation

deck = [17,13,11,2,3,5,7]
outputs = deckRevealedIncreasing(deck)