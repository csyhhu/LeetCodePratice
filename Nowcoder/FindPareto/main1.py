import sys 

def compareX(elem):
    return elem[0]

pos = []
# Read in data
f = open('./input.txt')
for idx, line in enumerate(f):
    line = line.rstrip('\n')
    # print(line)
    if idx == 0:
        N = int(line)
    else:
        x, y = line.split()
        pos.append([int(x), int(y)])

# print (pos)
visit = [1] * N
results = []
for i in range(N):
    # if visit[i] == 0:
    #   continue
    x1 = pos[i][0]
    y1 = pos[i][1]
    for j in range(N):
        # if i == j:
        #     break
        x2 = pos[j][0]
        y2 = pos[j][1]
        if x2>x1 and y2>y1:
            # print ('I am here')
            visit[i] = 0
            break
    if visit[i] == 1:
        results.append([pos[i][0], pos[i][1]])
# for i in range(N):
#     if visit[i] == 1:
#         print (pos[i][0], pos[i][1])
results.sort(key=compareX)
for r in results:
    print (r[0], r[1])
f.close()