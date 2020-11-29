def getSmallestString(n: int, k: int):
    cur_value = n # n instances of 'a'
    left_n = n
    cur_k = k
    offset_to_z = 25
    real_offset = 0
    while cur_value < cur_k:
        left_n -= 1
        if cur_value + offset_to_z >= cur_k:
            real_offset = cur_k - cur_value
            # print(cur_n, real_offset)
            break
        else:
            cur_value += offset_to_z

    result = 'a' * left_n + chr(ord('a') + real_offset) + 'z' * (n - left_n - 1)
    return result

print(getSmallestString(n = 3, k = 27))
print(getSmallestString(n = 5, k = 73))
print(getSmallestString(n = 10, k = 26 * 10))
print(getSmallestString(n = 10, k = 26 * 10))