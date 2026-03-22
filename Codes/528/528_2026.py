"""
LeetCode 528: Random Pick with Weight
https://leetcode.com/problems/random-pick-with-weight/

You are given a 0-indexed array of positive integers w where w[i] describes
the weight of the i-th index.

You need to implement the function pickIndex(), which randomly picks an index
in the range [0, w.length - 1] (inclusive) and returns it. The probability of
picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is
1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is
3 / (1 + 3) = 0.75 (i.e., 75%).

Example 1:
    Input:
        ["Solution","pickIndex"]
        [[[1]],[]]
    Output:
        [null,0]
    Explanation:
        Solution solution = new Solution([1]);
        solution.pickIndex(); // return 0. The only option is to return 0 since
                               // there is only one element in w.

Example 2:
    Input:
        ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
        [[[1,3]],[],[],[],[],[]]
    Output:
        [null,1,1,1,1,0]
    Explanation:
        Solution solution = new Solution([1, 3]);
        solution.pickIndex(); // return 1. It is returning the second element (index = 1)
                               // whose weight is 3. Its probability is 3/4 = 0.75.
        solution.pickIndex(); // return 1
        solution.pickIndex(); // return 1
        solution.pickIndex(); // return 0. It is returning the first element (index = 0)
                               // whose weight is 1. Its probability is 1/4 = 0.25.
        solution.pickIndex(); // return 1

Constraints:
    - 1 <= w.length <= 10^4
    - 1 <= w[i] <= 10^5
    - pickIndex will be called at most 10^4 times.

Hints:
    - Think about how to use the prefix sum of w.
    - If you have the prefix sum, how do you find which index a random number falls into?
    - Can you use binary search to speed things up?
"""
import random
from typing import List


class Solution:
    """
    # Brute force
    def __init__(self, w: List[int]):
        self.w_sum = sum(w)
        self.bucket = []
        for idx, weight in enumerate(w):
            for _ in range(weight):
                self.bucket.append(idx)
        print(self.bucket)

    def pickIndex(self) -> int:
        rand = int(random.random() * self.w_sum)
        return self.bucket[rand]
    """
    def __init__(self, w: List[int]):
        self.w_sum = sum(w)
        self.N = len(w)
        self.prefix_sum = []
        for idx, weight in enumerate(w):
            if idx == 0:
                self.prefix_sum.append(weight)
            else:
                self.prefix_sum.append(self.prefix_sum[-1] + weight)

    def binary_search(self, target, left, right):
        """
        print(target, left, right)
        # left reach to the end
        if left >= right:
            return left
        if self.prefix_sum[left] <= target < self.prefix_sum[left+1]:
            return left
        mid = (left + right) // 2
        if target > self.prefix_sum[mid]:
            return self.binary_search(target, mid + 1, right)
        else:
            return self.binary_search(target, left, mid)
        """
        while left < right:
            mid = (left + right) // 2
            if target > self.prefix_sum[mid]:
                left = mid + 1
            else:
                right = mid
        return left

    def pickIndex(self) -> int:
        rand = random.random() * self.w_sum
        return self.binary_search(rand, 0, self.N - 1)
        


# Test: verify weighted distribution
if __name__ == "__main__":
    import collections

    # Test 1: w = [1, 3], expected ~25% index 0, ~75% index 1
    solution = Solution([1, 3])
    N = 100000
    counts = collections.Counter()
    for _ in range(N):
        counts[solution.pickIndex()] += 1

    print("=" * 55)
    print("LeetCode 528: Random Pick with Weight")
    print(f"w = [1, 3], Total samples: {N}")
    print("=" * 55)
    expected = {0: 25.0, 1: 75.0}
    for idx in sorted(counts):
        pct = counts[idx] / N * 100
        exp = expected.get(idx, 0)
        deviation = abs(pct - exp)
        status = "✅" if deviation < 2.0 else "⚠️ "
        print(f"  index {idx}: {counts[idx]:6d} times  ({pct:.2f}%)  expected {exp:.1f}%  {status}")

    print()

    # Test 2: w = [1, 2, 3], expected ~16.7%, ~33.3%, ~50%
    solution2 = Solution([1, 2, 3])
    counts2 = collections.Counter()
    for _ in range(N):
        counts2[solution2.pickIndex()] += 1

    print(f"w = [1, 2, 3], Total samples: {N}")
    print("=" * 55)
    expected2 = {0: 100/6, 1: 200/6, 2: 300/6}
    for idx in sorted(counts2):
        pct = counts2[idx] / N * 100
        exp = expected2.get(idx, 0)
        deviation = abs(pct - exp)
        status = "✅" if deviation < 2.0 else "⚠️ "
        print(f"  index {idx}: {counts2[idx]:6d} times  ({pct:.2f}%)  expected {exp:.1f}%  {status}")
