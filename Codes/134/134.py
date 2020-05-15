def canCompleteCircuit(gas, cost):

    gain = [a-b for (a, b) in zip(gas, cost)]

    def loop(start):
        cur_idx = start
        left = 0
        canComplete = True
        while cur_idx != start-1:
            left += (gas[cur_idx] - cost[cur_idx])
            if left < 0:
                canComplete = False
                break
            cur_idx = (cur_idx + 1) % len(gas)

        return canComplete

    for idx, g in enumerate(gain):
        if g > 0:
            if loop(idx):
                return idx

    return -1

def canCompleteCircuit2(gas, cost):

    start = 0
    left = 0 # Current remaining gas
    lack = 0 # How much gas is in debt

    for i in range(len(gas)):

        left += (gas[i] - cost[i])
        if left < 0:
            start = i + 1
            lack += left
            left = 0

    if left + lack >= 0:
        return start
    else:
        return -1

solution = canCompleteCircuit

print(solution([1,2,3,4,5], [3,4,5,1,2]))
print(solution([4,5,2,6,5,3], [3,2,7,3,2,9]))