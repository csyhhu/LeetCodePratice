def kthSmallestPrimeFraction_TLE(A, K: int):

    if len(A) == 0:
        return [0, 0]

    n = len(A)
    l = 0
    r = 1
    max_break_point = 0
    k_denominator = k_numerator = 0
    while l < r:
        max_break_point = 0
        k_denominator = k_numerator = 0
        mid = (l + r) / 2
        # Get the number of faction before mid
        n_count = 0
        for denominator_idx in range(n-1, 0, -1):
            for numerator_idx in range(denominator_idx-1, -1, -1):
                # print(denominator_idx, numerator_idx)
                break_point = A[numerator_idx] / A[denominator_idx]
                if break_point < mid:
                    n_count += (numerator_idx + 1) # Include itself

                    if break_point > max_break_point:
                        max_break_point = break_point
                        k_denominator = A[denominator_idx]
                        k_numerator = A[numerator_idx]
                        # print(k_denominator, k_numerator)
                    break
        # print(n_count)
        if n_count == K:
            break
        elif n_count < K:
            l = mid
        else:
            r = mid

    return [k_numerator, k_denominator]


def kthSmallestPrimeFraction(A, K: int):

    if len(A) == 0:
        return [0, 0]

    n = len(A)
    l = 0
    r = 1
    max_break_point = 0
    k_denominator = k_numerator = 0
    while l < r:
        max_break_point = 0
        k_denominator = k_numerator = 0
        mid = (l + r) / 2
        # Get the number of faction before mid
        n_count = 0
        numerator_idx = n-2
        for denominator_idx in range(n-1, 0, -1):
            # for numerator_idx in range(denominator_idx-1, -1, -1):
            while numerator_idx >= 0:
                # print(denominator_idx, numerator_idx)
                break_point = A[numerator_idx] / A[denominator_idx]
                if break_point < mid:
                    n_count += (numerator_idx + 1) # Include itself

                    if break_point > max_break_point:
                        max_break_point = break_point
                        k_denominator = A[denominator_idx]
                        k_numerator = A[numerator_idx]
                    break
                numerator_idx -= 1
        # print(n_count)
        if n_count == K:
            break
        elif n_count < K:
            l = mid
        else:
            r = mid

    return [k_numerator, k_denominator]

print(kthSmallestPrimeFraction(A = [1, 2, 3, 5], K = 3))
print(kthSmallestPrimeFraction(A = [1, 7], K = 1))
print(kthSmallestPrimeFraction([1,29,47], 1))

