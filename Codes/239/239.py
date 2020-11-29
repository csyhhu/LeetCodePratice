def maxSlidingWindow_TLE(nums, k: int):

    results = []
    n = len(nums)
    for i in range(n - k + 1):
        """
        if i + k >= n - 1:
            results.append(max(nums[i:]))
            break
        else:
            results.append(max(nums[i:i+k]))
        """
        results.append(max(nums[i:i+k]))
        # print(results)
    return results


def maxSlidingWindow(nums, k):
    # import collections
    class monotonicQueue():
        def __init__(self):
            self.q_ = []
        def push(self, value):
            while len(self.q_) > 0 and self.q_[-1] < value:
                self.q_.pop(-1)
            self.q_.append(value)
        def top(self):
            return self.q_[0]
        def pop(self):
            self.q_.pop(0)

    ans = []
    n = len(nums)
    queue = monotonicQueue()
    for i in range(n):
        queue.push(nums[i])
        if i >= k - 1:
            ans.append(queue.top())
            if nums[i - k + 1] == queue.top():
                queue.pop()

    return ans


print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(maxSlidingWindow(nums = [1], k = 1))
print(maxSlidingWindow(nums = [1,-1], k = 1))
print(maxSlidingWindow(nums = [9,11], k = 2))
print(maxSlidingWindow(nums = [4,-2], k = 2))