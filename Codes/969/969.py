def pancakeSort(A):
    N = len(A)
    results = []
    for value in range(N, 0, -1):
        # print(A)
        idx = A.index(value)
        # First time reverse
        A[0:idx+1] = A[idx::-1]
        # print(A)
        results.append(idx+1)
        # Second time reverse
        A[0:value] = A[value-1::-1]
        # print(A)
        results.append(value)
    return results

inputs = [3,2,4,1]
outputs = pancakeSort(inputs)
print(outputs)