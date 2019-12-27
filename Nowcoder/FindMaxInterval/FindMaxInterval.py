f = open('./input.txt')
array = []
N = 0
for idx, line in enumerate(f):
    line = line.rstrip('\n')
    if idx == 0:
    	N = int(line)
    else:
    	for l in line.split():
    		array.append(int(l))
print(array)

