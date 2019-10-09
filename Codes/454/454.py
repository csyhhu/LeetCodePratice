def fourSumCount(A, B, C, D):
    ab_dict = {}
    for a in A:
        for b in B:
            # ab_dict[(a,b)] = a+b
            if a+b in ab_dict:
                ab_dict[a+b] += 1
            else:
                ab_dict[a+b] = 1
    # print(ab_dict)

    results = 0
    for c in C:
        for d in D:
            # cd = c+d
            # if cd in ab_dict.values():
            # results += sum(map((-c-d).__eq__, ab_dict.values()))
            if -c-d in ab_dict:
                results += ab_dict[-c-d]

    return results

# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]

A = [-1,-1]
B = [-1,1]
C = [-1,1]
D = [1,-1]
print(fourSumCount(A,B,C,D))