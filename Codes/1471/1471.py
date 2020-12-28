def getStrongest_1(arr: list, k: int):

    n = len(arr)
    arr.sort()
    median = arr[(n-1)//2]

    strength = []
    for a in arr:
        strength.append([a, abs(a - median)])

    import functools
    def cmp(a, b):
        v_a, dist_a = a
        v_b, dist_b = b
        if dist_a < dist_b:
            return 1
        elif dist_a == dist_b:
            return 1 if v_a < v_b else -1
        else:
            return -1
    # print(strength)
    strength.sort(key=functools.cmp_to_key(cmp))
    # print(strength)
    ans = []
    for i in range(k):
        ans.append(strength[i][0])

    return ans


def swap(_arr:list, i:int, j:int):
    temp = _arr[i]
    _arr[i] = _arr[j]
    _arr[j] = temp


def quickSelection(_arr, left, right):
    """
    This function arranges all elements smaller than left to left side and larger than left to right size.
    Return a semi-ordered list like: [3,1,0,2, 5, 8,6,9,7] and the index of 5
    :param _arr:
    :param left:
    :param right:
    :return:
    """
    start = left + 1
    end = right
    while True:
        # Start pointer move forward to where element is larger than left
        while start < right and _arr[start] <= _arr[left]:
            start += 1
        # End pointer move backward to where element is smaller than left
        while left < end and _arr[end] >= _arr[left]:
            end -= 1
        # If start goes to -1 or end goes to 0, it means all elements are ordered
        if start >= end:
            break
        # Swap the unordered elements to make sure (<)start is smaller than left and (>)end is larger than left
        swap(_arr, start, end)
        # print(_arr)
    # Swap left (pivot) with end pointer
    swap(_arr, left, end)
    return end


def kthSmallest(_arr, _k):
    left, right = 0, len(_arr) - 1
    # mid = (left + right) // 2
    while left < right:
        mid = quickSelection(_arr, left, right)
        if mid == _k:
            return _arr[mid]
        elif mid > _k:
            right = mid - 1
        else:
            left = mid + 1
        # print(left, mid, right)
    return _arr[left]


def getStrongest_2(arr: list, k: int):

    n = len(arr)

    median = kthSmallest(arr, (n-1) // 2)
    # print(arr, median)

    strength = []
    for a in arr:
        strength.append([a, abs(a - median)])

    import functools
    def cmp(a, b):
        v_a, dist_a = a
        v_b, dist_b = b
        if dist_a < dist_b:
            return 1
        elif dist_a == dist_b:
            return 1 if v_a < v_b else -1
        else:
            return -1
    # print(strength)
    strength.sort(key=functools.cmp_to_key(cmp))
    # print(strength)
    ans = []
    for i in range(k):
        ans.append(strength[i][0])

    return ans


def getStrongest(arr: list, k: int):

    pass

print(getStrongest(arr = [1,2,3,4,5], k = 2))
print(getStrongest(arr = [1,1,3,5,5], k = 2))
print(getStrongest(arr = [6,7,11,7,6,8], k = 5))
print(getStrongest(arr = [6,-3,7,2,11], k = 3))
print(getStrongest(arr = [-7,22,17,3], k = 2))

# print(kthSmallest([6,7,11,7,6,8], 5))