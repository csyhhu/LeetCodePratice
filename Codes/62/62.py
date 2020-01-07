def uniquePaths(m, n):
    import math
    a = m - 1
    b = n - 1

    return int(math.factorial(a+b) / (math.factorial(b) * math.factorial(a)))


m = 7
n = 3
print(uniquePaths(m, n))