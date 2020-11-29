def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    consecutive_range = dict()
    for num in nums:
        # """
        num_exist = False
        for start, range_len in consecutive_range.items():
            if num == start - 1:
                consecutive_range[num] = (range_len + 1)
                consecutive_range.pop(start)
                num_exist = True
                """
                new_end = consecutive_range[num] + num
                while new_end in consecutive_range:
                    consecutive_range[start - 1] += consecutive_range[new_end]
                    consecutive_range.pop(new_end)
                    new_end = consecutive_range[start - 1] + start - 1
                break
                """
                new_start = num
                # union = False
                for other_start, other_range_len in consecutive_range.items():
                    if new_start == other_start + other_range_len:
                        consecutive_range[other_start] += consecutive_range[new_start]
                        # union = True
                        consecutive_range.pop(new_start)
                        break
                # if union:
                break

            elif num == (start + range_len):
                consecutive_range[start] += 1
                num_exist = True
                new_end = consecutive_range[start] + start
                while new_end in consecutive_range:
                    consecutive_range[start] += consecutive_range[new_end]
                    consecutive_range.pop(new_end)
                    new_end = consecutive_range[start] + start
                break
            elif start - 1 < num < start + range_len:
                num_exist = True
                break
        if not num_exist:
            consecutive_range[num] = 1
        # """
        # print(consecutive_range)
    return max(consecutive_range.values())

print(longestConsecutive(nums = [100,4,200,1,3,2]))
print(longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))