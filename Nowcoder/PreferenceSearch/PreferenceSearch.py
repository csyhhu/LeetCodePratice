# f = open('./input.txt')
# # print(f.readline().strip('\n'))
# n = int(f.readline().strip('\n'))
# preference = [int(p) for p in f.readline().strip('\n').split()]
# q = int(f.readline().strip('\n'))
#
# def compareFirst(elem):
#     return elem[0]
# pref_dict = {}
# import numpy as np
# for p in np.unique(preference):
# 	pref_dict[p] = 0
# query_list = []
# for _ in range(q):
# 	line = f.readline().strip('\n').split()
# 	l, r, k = int(line[0]), int(line[1]), int(line[2])
# 	query_list.append([l-1, r-1, k])
# query_list.sort(key=compareFirst)
#
# for query_idx in range(0, len(query_list)):
# 	l, r, k = query_list[query_idx]
# 	# count = 0
# 	if query_idx == 0:
# 		for i in range(l, r + 1):
# 			pref_dict[preference[i]] += 1
# 	else:
# 		prev_l, prev_r, _ = query_list[query_idx - 1]
# 		if prev_r > l:
# 			for i in range(prev_l, l):
# 				pref_dict[preference[i]] -= 1
# 			for i in range(prev_r, r+1):
# 				pref_dict[preference[i]] += 1
# 		else:
# 			for i in range(l, r+1):
# 				if pref_dict[preference[i]] == 0:
# 					pref_dict[preference[i]] += 1
# 				else:
# 					pref_dict[preference[i]] = 1
# 	print (pref_dict[k])


"""
# Execution Time Exceed
l, r, k = int(line[0]), int(line[1]), int(line[2])
count = 0
for i in range(l, r+1):
	if preference[i-1] == k:
		count += 1
print(count)
"""

import sys
import numpy as np
def compareFirst(elem):
    return elem[0]

n = int(sys.stdin.readline().strip('\n'))
preference = [int(p) for p in sys.stdin.readline().strip('\n').split()]
q = int(sys.stdin.readline().strip('\n'))
query_list = []
pref_dict = {}
for p in np.unique(preference):
    pref_dict[p] = 0
for  _ in range(q):
    line = sys.stdin.readline().strip('\n').split()
    l, r, k = int(line[0]), int(line[1]), int(line[2])
    query_list.append([l-1, r-1, k])
query_list.sort(key=compareFirst)

for query_idx in range(0, len(query_list)):
    l, r, k = query_list[query_idx]
    # count = 0
    if query_idx == 0:
        for i in range(l, r + 1):
            pref_dict[preference[i]] += 1
    else:
        prev_l, prev_r, _ = query_list[query_idx - 1]
        if prev_r > l:
            for i in range(prev_l, l):
                pref_dict[preference[i]] -= 1
            for i in range(prev_r, r+1):
                pref_dict[preference[i]] += 1
        else:
            for i in range(l, r+1):
                if pref_dict[preference[i]] == 0:
                    pref_dict[preference[i]] += 1
                else:
                    pref_dict[preference[i]] = 1
    print (pref_dict[k])
# print (l,r,k)
# count = 0
# for i in range(l, r+1):
# 	if prefernce[i-1] == k:
# 		count += 1
# print(count)