def searchRange_lineSearch(nums, target):

    def dichotomy(arr, start, end, tar):

        mid = (end - start) // 2 + start

        if start == end:
            return -1, -1

        if arr[mid] < tar:
            left, right = dichotomy(arr, mid + 1, end, tar)
        elif arr[mid] > tar:
            left, right = dichotomy(arr, start, mid, tar)
        else:
            left = mid
            right = left
            for i in range(mid, end):
                if arr[i] != tar:
                    right = i - 1
                    break
                else:
                    right = i

            for i in range(mid - 1, start - 1, -1): # start - 1 means start need to be taken
                if arr[i] != tar:
                    left = i + 1
                    break
                else:
                    left = i

        return left, right

    return dichotomy(nums, 0, len(nums), target)


def searchRange(nums, target):

    def findFirstPos(nums, target):
        """
        Fine the lower bound of the array formed by target
        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(nums)
        while start < end:
            mid = (end + start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid + 1
        if start == len(nums) or nums[start] != target:
            return -1
        else:
            return start

    def findLastPos(nums, target):
        """
        Fine the upper bound of the array formed by target
        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(nums)
        while start < end:
            mid = (end + start) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid + 1
        start -= 1
        if start < 0 or nums[start] != target:
            return -1
        else:
            return start

    return findFirstPos(nums, target), findLastPos(nums, target)

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))

nums = [5,7,7,8,8,10]
target = 6
print(searchRange(nums, target))

nums = []
target = 6
print(searchRange(nums, target))

nums = [1]
target = 1
print(searchRange(nums, target))

nums = [2,2]
target = 2
print(searchRange(nums, target))