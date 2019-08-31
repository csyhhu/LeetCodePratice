def merge(intervals):

    results = []
    starts = []
    ends = []
    for int in intervals:
        starts.append(int[0])
        ends.append(int[1])
    starts = sorted(starts)
    ends = sorted(ends)

    start_idx = 0
    for end_idx, end in enumerate(ends):
        if end_idx == (len(ends)-1) or end < starts[end_idx + 1]:
            results.append([starts[start_idx], end])
            start_idx = end_idx + 1

    return results


def merge2(intervals):

    # def interval_cmp(int1, int2):
    #     if int1[0] < int2[0]:
    #         return True
    #     elif int1[0] == int2[0]:
    #         return int1[1] < int2[1]
    #     else:
    #         return False

    if len(intervals) == 0:
        return intervals

    intervals.sort(key=lambda tup: tup[0])

    results = [intervals[0]]

    for inter in intervals[1:]:
        tail = results[-1]
        # Tell intersection
        # 1. [1,4] [2,5]
        # 2. [1,4] [2,4]
        # 3. [1,4] [1,4]
        if (inter[0] <= tail[1]) and (inter[1] >= tail[1]):
            results[-1][1] = inter[1]
        # Tell incorpration
        elif inter[0] >= tail[0] and inter[1] <= tail[1]:
            pass
        else:
            results.append(inter)

    return results


inputs = [[1,3],[8,10],[15,18],[2,6]]
outputs = merge2(inputs)
# outputs = merge(inputs)
print(outputs)
