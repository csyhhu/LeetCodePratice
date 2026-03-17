"""
[56] Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    - 1 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i <= end_i <= 10^4

Date: 2026-03-08
"""

from operator import le


def merge(intervals):
    # Sort intervals by left
    intervals = sorted(intervals, key=lambda x: x[0])
    # Iterate intervals by examining whether the right end covers the left end of the next interval
    result = []
    n = len(intervals)
    result.append(intervals[0])
    for i in range(1, n):
        prev_right = result[-1][1]
        cur_left = intervals[i][0]
        # Merge i-th intervals if overlap by expanding the i-1 th's right end to itself or i-th's right
        if prev_right >= cur_left:
            result[-1][1] = max(prev_right, intervals[i][1])
        # If not overlap, put it into result
        else:
            result.append(intervals[i])
        # print(result)
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,2],[3,4]], [[1,2],[3,4]]),
        ([[1,5]], [[1,5]]),
        ([[1,5],[2,3]], [[1,5]]),
        ([[0,0]], [[0,0]]),
        ([[2,3],[4,5],[6,7],[8,9],[1,10]], [[1,10]])
    ]
    
    print("=" * 70)
    print("LeetCode 56 - Merge Intervals")
    print("=" * 70)
    
    for intervals, expected in test_cases:
        try:
            result = merge(intervals)
            if result is None:
                print(f"⚠️  intervals={intervals} -> Not implemented")
            else:
                # 排序比较结果
                result_sorted = sorted(result)
                expected_sorted = sorted(expected)
                is_correct = result_sorted == expected_sorted
                status = "✓" if is_correct else "✗"
                print(f"{status} intervals={intervals}")
                print(f"   Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"❌ intervals={intervals} -> Error: {e}")
