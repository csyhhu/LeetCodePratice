f = open('./input.txt')
# print(f.readline().strip('\n'))
n = int(f.readline().strip('\n'))
preference = [int(p) for p in f.readline().strip('\n').split()]
q = int(f.readline().strip('\n'))
for _ in range(q):
	line = f.readline().strip('\n').split()
	"""
	# Execution Time Exceed
	l, r, k = int(line[0]), int(line[1]), int(line[2])
	count = 0
	for i in range(l, r+1):
		if preference[i-1] == k:
			count += 1
	print(count)
	"""


# import sys
# n = int(sys.stdin.readline().strip('\n'))
# prefernce = [int(p) for p in sys.stdin.readline().strip('\n').split()]
# q = int(sys.stdin.readline().strip('\n'))
# for  _ in range(q):
# 	line = sys.stdin.readline().strip('\n').split()
# 	l, r, k = int(line[0]), int(line[1]), int(line[2])
# 	count = 0
# 	for i in range(l, r+1):
# 		if prefernce[i-1] == k:
# 			count += 1
# 	print(count)