def intervalIntersection_Wrong(A, B):
    MAX_LEN = 1001
    list1 = [0] * MAX_LEN
    list2 = [0] * MAX_LEN
    for start, end in A:
        list1[start: end+1] = [1] * (end + 1 - start)
    for start, end in B:
        list2[start: end+1] = [1] * (end + 1 - start)

    overlap = [i+j for (i,j) in zip(list1,list2)]
    print(list1[0: 27])
    print(list2[0: 27])
    print(overlap[0: 27])

    results = []
    idx = 0
    start_flag = False
    while idx < MAX_LEN:

        if not start_flag and overlap[idx] == 2:
            start = idx
            start_flag = True

        if start_flag and overlap[idx] != 2:
            end = idx-1
            results.append([start, end])
            start_flag = False
        idx += 1
    return results


def intervalIntersection(A, B):

    idx_A = 0
    idx_B = 0
    results = []
    while idx_A < len(A) and idx_B < len(B):
        startA, endA = A[idx_A]
        startB, endB = B[idx_B]

        lo = max(startA, startB)
        hl = min(endA, endB)

        if lo <= hl:
            results.append([lo, hl])

        if endA < endB:
            idx_A += 1
        else:
            idx_B += 1

    return results



A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
outputs = intervalIntersection(A, B)
print(outputs)
