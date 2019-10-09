def shipWithinDays(weights, D):
    """
    Binary search, upper bound must be sum(weights), lower bound is the max(weights).
    Setting a variable named res to store the possible answer
    :param weights:
    :param D:
    :return:
    """

    def allocateWeights(weights, D, conveyor):
        cur = conveyor
        day_used = 1
        for w in weights:
            if w <= cur:
                cur -= w
            else:
                cur = conveyor - w
                day_used += 1
                if day_used > D:
                    return False
        return True

    upper = sum(weights)
    lower = max(weights)

    res = upper # Key!

    while lower <= upper:

        mid = (lower + upper) // 2
        feasible = allocateWeights(weights, D, mid)
        # print(lower, upper, mid, feassible)
        if feasible:
            upper = mid - 1
            res = mid
        else:
            lower = mid + 1

    return res

weights = [1,2,3,4,5,6,7,8,9,10]
D = 5

# weights = [3,2,2,4,1,4]
# D = 3

print(shipWithinDays(weights, D))