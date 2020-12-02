def getSkyline(buildings):
    events = []
    for start, end, height in buildings:
        events.append([start, height, 'enter'])
        events.append([end, height, 'leave'])

    import functools
    def cmp(e1, e2):
        """
        if e1[0] > e2[0]:
            return 1
        elif e1[0] == e2[0]:
            if e1[1] < e2[1]:
                return 1
            else:
                return -1
        else:
            return -1
        """
        if e1[0] != e2[0]:
            return -1 if e1[0] < e2[0] else 1

        if e1[2] == e2[2] == 'leave':
            return -1 if e1[1] < e2[1] else 1

        if e1[2] == e2[2] == 'enter':
            return -1 if e1[1] > e2[1] else 1

        # if e1[2] == e2[2]:
        #     return -1 if e1[1] < e2[1] else 1

        return -1 if e1[2] is 'enter' else 1

    events.sort(key=functools.cmp_to_key(cmp))
    # print(events)
    maxHeap = []
    ans = []
    import heapq
    for event in events:
        print(event)
        # If it is an enter event, add the height to the max heap.
        # And find out whether the current height is the highest, if so, add it to the current ans
        if event[2] == 'enter':
            cur_max_height = - maxHeap[0] if maxHeap else 0
            heapq.heappush(maxHeap, - event[1])
            if cur_max_height < event[1]:
                ans.append([event[0], event[1]])
        # If it is a leave event, let's see what happen after we remove it. If the max height become less,
        # that means we need to add this second height to the ans
        elif event[2] == 'leave':
            # Here I should remove the height corresponding to the current event
            heapq.heappop(maxHeap)
            second_max_height = - maxHeap[0] if maxHeap else 0
            if second_max_height <= event[1]:
                ans.append([event[0], second_max_height])
        print(maxHeap)
        print(ans)
        print('---')
    return ans


def getSkyline_WA(buildings):
    """
    Copied from online and it is wrong
    :param buildings:
    :return:
    """
    class Edge(object):
        def __init__(self, x, height, is_start):
            self.x = x
            self.height = height
            self.is_start = is_start

        def __repr__(self):
            return repr((self.x, self.height, self.is_start))

    def compare(edge1, edge2):
        if edge1.x != edge2.x:
            return -1 if edge1.x < edge2.x else 1

        if ((edge1.is_start and edge2.is_start) or
                (not edge1.is_start and not edge2.is_start)):
            return -1 if edge1.height < edge2.height else 1

        return -1 if edge1.is_start else 1

    import functools
    from heapq import heappop, heappush
    edges = []
    for building in buildings:
        start_edge = Edge(building[0], building[2], True)
        end_edge = Edge(building[1], building[2], False)
        edges.extend((start_edge, end_edge))
    sorted_edges = sorted(edges, key=functools.cmp_to_key(compare))
    maxHeap, result = [], []
    for edge in sorted_edges:
        if edge.is_start:
            if not maxHeap or edge.height > - maxHeap[0]:
                result.append((edge.x, edge.height))
            heappush(maxHeap, - edge.height)
        else:
            heappop(maxHeap)
            if not maxHeap:
                result.append((edge.x, 0))
            elif edge.height > - maxHeap[0]:
                result.append((edge.x, - maxHeap[0]))

    return result


# print(getSkyline(buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
# print(getSkyline(buildings = [[0,2,3],[2,5,3]]))
print(getSkyline([[1,2,1],[1,2,2],[1,2,3]]))