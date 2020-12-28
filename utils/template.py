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
    mid = (left + right) // 2
    while left <= right:
        mid = quickSelection(_arr, left, right)
        if mid == _k:
            return _arr[mid]
        elif mid > _k:
            right = mid - 1
        else:
            left = mid + 1
    return mid