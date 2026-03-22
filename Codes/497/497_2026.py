"""
LeetCode 497: Random Point in Non-overlapping Rectangles
https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

You are given an array of non-overlapping axis-aligned rectangles rects where
rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left corner
point of the ith rectangle and (xi, yi) is the top-right corner point of the
ith rectangle. Design an algorithm to pick a random integer point inside the
space covered by one of the given rectangles. A point on the perimeter of a
rectangle is included in the space covered by the rectangle.

Any integer point inside the space covered by one of the given rectangles
should be equally likely to be returned.

Note: an integer point is a point that has integer coordinates.

Example 1:
    Input:
        ["Solution", "pick", "pick", "pick", "pick", "pick"]
        [[[[−2,−2,1,1],[2,2,4,4]]], [], [], [], [], []]
    Output:
        [null, [1,−2], [1,4], [−1,−1], [0,0], [3,3]]

Constraints:
    - 1 <= rects.length <= 100
    - rects[i].length == 4
    - -10^9 <= ai < xi <= 10^9
    - -10^9 <= bi < yi <= 10^9
    - All the rectangles do not overlap.
    - At most 10^4 calls will be made to pick.

Hints:
    - Think of each rectangle as having (xi - ai + 1) * (yi - bi + 1) integer points.
    - This is very similar to LeetCode 528: random pick with weight.
    - Use prefix sum of "areas" (number of integer points) to decide which rectangle to pick.
    - Then uniformly pick a random integer point inside the chosen rectangle.
"""
import random
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        # TODO: Build prefix sum of integer point counts per rectangle
        # Hint: area of rect [a,b,x,y] = (x-a+1) * (y-b+1)
        self.rects = rects
        self.rects_sum = 0
        self.prefix_sum = []
        self.N = len(rects)
        for rect in rects:
            self.rects_sum += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.prefix_sum.append(self.rects_sum)

    def binary_search(self, target, left, right):
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sum[mid] < target:
                return self.binary_search(target, mid + 1, right)
            else:
                return self.binary_search(target, left, mid)
        return left

    def pick(self) -> List[int]:
        # TODO:
        # Step 1: Use binary search on prefix sum to pick a weighted-random rectangle
        # Step 2: Uniformly pick a random integer point inside the chosen rectangle
        rand = random.random() * self.rects_sum
        idx = self.binary_search(rand, 0, self.N - 1)
        # print(idx, self.rects[idx])
        rand_x = random.randint(self.rects[idx][0], self.rects[idx][2])
        rand_y = random.randint(self.rects[idx][1], self.rects[idx][3])
        return [rand_x, rand_y]


# Test cases
if __name__ == "__main__":
    import collections

    # Test 1: two small rectangles
    # rect A: [-2,-2,1,1] => (1-(-2)+1)*(1-(-2)+1) = 4*4 = 16 points
    # rect B: [2,2,4,4]   => (4-2+1)*(4-2+1) = 3*3 = 9 points
    # total 25 points, ~64% in A, ~36% in B
    rects = [[-2, -2, 1, 1], [2, 2, 4, 4]]
    sol = Solution(rects)

    N = 10000
    rect_counts = collections.Counter()
    for _ in range(N):
        p = sol.pick()
        x, y = p
        if -2 <= x <= 1 and -2 <= y <= 1:
            rect_counts["A"] += 1
        elif 2 <= x <= 4 and 2 <= y <= 4:
            rect_counts["B"] += 1
        else:
            print(f"❌ Point {p} is out of all rectangles!")

    print("=" * 55)
    print("LeetCode 497: Random Point in Non-overlapping Rectangles")
    print(f"Total samples: {N}")
    print("=" * 55)
    print(f"  Rect A [-2,-2,1,1]: {rect_counts['A']:5d} times  ({rect_counts['A']/N*100:.2f}%)  expected ~64.00%")
    print(f"  Rect B [2,2,4,4]:   {rect_counts['B']:5d} times  ({rect_counts['B']/N*100:.2f}%)  expected ~36.00%")

    # Test 2: single rectangle
    sol2 = Solution([[1, 1, 5, 5]])
    seen = set()
    for _ in range(10000):
        p = sol2.pick()
        x, y = p
        assert 1 <= x <= 5 and 1 <= y <= 5, f"Point {p} out of rect [1,1,5,5]"
        seen.add((x, y))
    print(f"\nTest 2 single rect [1,1,5,5]: {len(seen)} distinct integer points seen (expected 25)")
