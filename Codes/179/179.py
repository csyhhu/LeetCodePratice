def largestNumber0(nums):
    from functools import cmp_to_key

    def cmp(a, b):
        """
        Compare the high digit of two number
        :param a:
        :param b:
        :return:
        """
        # Convert a and b to list
        a_list = []
        while a != 0:
            a_list.append(a % 10)
            a = a // 10
        b_list = []
        while b != 0:
            b_list.append(b % 10)
            b = b // 10

        a_list.reverse()
        b_list.reverse()
        # print(a_list, b_list)

        min_len = min(len(a_list), len(b_list))
        for i in range(min_len):
            if a_list[i] != b_list[i]:
                #  print(a_list[i], b_list[i])
                if a_list[i] > b_list[i]:
                    return 1
                else:
                    return -1
        # print('----')
        if len(a_list) < len(b_list):
            return 1
        elif len(a_list) > len(b_list):
            return -1
        else:
            return 0

    # nums.sort(cmp=cmp)
    # return nums
    sorted_nums = sorted(nums, key=cmp_to_key(cmp), reverse=True)
    # print(result)
    # print(nums)
    result = ''
    for s in sorted_nums:
        result += str(s)
    return result


def largestNumber(nums):
    from functools import cmp_to_key
    def cmp(a, b):
        # return a + b > b + a
        if a + b > b + a :
            return 1
        elif a + b < b + a :
            return -1
        else:
            return 0

    nums_str = list(map(str, nums))
    nums_str.sort(key=cmp_to_key(cmp), reverse=True)
    result = ''.join(nums_str).lstrip('0')
    return result if result else '0'

nums = [3,30,34,5,9]
print(largestNumber0(nums))

nums = [10,2]
print(largestNumber0(nums))
