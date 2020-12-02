def removeCoveredIntervals(intervals: list):
    import functools
    def cmp(interv1, interv2):
        if interv1[0] < interv2[0]:
            return -1
        elif interv1[0] == interv2[0]:
            if interv1[1] > interv2[1]:
                return -1
            else:
                return 1
        else:
            return 1

    intervals.sort(key=functools.cmp_to_key(cmp))
    count = 0
    max_end = 0
    for cur_start, cur_end in intervals:
        if max_end < cur_end:
            count += 1
            max_end = cur_end
    return count

print(removeCoveredIntervals([[1,4],[3,6],[2,8]]))
print(removeCoveredIntervals(intervals = [[1,4],[2,3]]))
print(removeCoveredIntervals(intervals = [[3,10],[4,10],[5,11]]))