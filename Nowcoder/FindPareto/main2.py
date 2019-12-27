
def compareX(elem):
    return elem[0]

pos = []
f = open('./input.txt')
for idx, line in enumerate(f):
    line = line.rstrip('\n')
    if idx == 0:
        N = int(line)
    else:
        x, y = line.split()
        pos.append([int(x), int(y)])

pos.sort(key=compareX, reverse=True)

results = []
maxy = -1
for p in pos:
	x, y = p[0], p[1]
	if y > maxy:
		maxy = y
		results.append([x, y])
for r in results[::-1]:
	print (r[0], r[1])