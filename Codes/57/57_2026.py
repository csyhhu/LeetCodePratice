"""
[57] Insert Interval
https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i]
represent the start and the end of the ith interval and intervals is sorted in ascending order by
start_i. You are also given an interval newInterval = [start, end] that represents the start and
end of another interval.

Insert newInterval into intervals such that:
1. intervals is still sorted in ascending order by start_i.
2. intervals still does not contain any overlapping intervals (merge overlapping intervals if necessary).

Return the resulting intervals.

Note: intervals is NOT modified in place. You should return a new array.

Example 1:
    Input: intervals = [[1,5]], newInterval = [2,7]
    Output: [[1,7]]

Example 2:
    Input: intervals = [[1,2],[3,5],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 3:
    Input: intervals = [[1,2],[3,5],[6,9]], newInterval = [2,10]
    Output: [[1,10]]

Example 4:
    Input: intervals = [[2,5],[6,9]], newInterval = [1,4]
    Output: [[1,5],[6,9]]

Example 5:
    Input: intervals = [[3,5],[6,9]], newInterval = [1,2]
    Output: [[1,2],[3,5],[6,9]]

Constraints:
    - 0 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i <= end_i <= 10^5
    - newInterval.length == 2
    - 0 <= start <= end <= 10^5

Date: 2026-03-08
"""


from calendar import c


def insert(intervals, newInterval):
    """
    Insert a new interval into a list of non-overlapping intervals and merge if necessary.
    
    Args:
        intervals: List of non-overlapping intervals sorted by start time
        newInterval: The interval to insert
    
    Returns:
        List of intervals after insertion and merging
    """
    n = len(intervals)
    result = []
    i = 0
    # Linear search and add all intervals that is behind new interval.
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    # Process the over-lapping part: expanding the new interval
    while i < n and intervals[i][0] <= newInterval[1]:
        left, right = intervals[i]
        newInterval[0] = min(left, newInterval[0])
        newInterval[1] = max(right, newInterval[1])
        i += 1
    result.append(newInterval)
    # Add the rest normal intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1,5]], [2,7], [[1,7]]),
        ([[1,2],[3,5],[6,9]], [2,5], [[1,5],[6,9]]),
        ([[1,2],[3,5],[6,9]], [2,10], [[1,10]]),
        ([[2,5],[6,9]], [1,4], [[1,5],[6,9]]),
        ([[3,5],[6,9]], [1,2], [[1,2],[3,5],[6,9]]),
        ([], [5,7], [[5,7]]),
        ([[1,10]], [2,3], [[1,10]]),
        ([[1,5]], [0,0], [[0,0],[1,5]]),
    ]
    
    print("=" * 70)
    print("LeetCode 57 - Insert Interval")
    print("=" * 70)
    
    for intervals, newInterval, expected in test_cases:
        try:
            result = insert(intervals, newInterval)
            if result is None:
                print(f"⚠️  intervals={intervals}, newInterval={newInterval} -> Not implemented")
            else:
                is_correct = result == expected
                status = "✓" if is_correct else "✗"
                print(f"{status} intervals={intervals}, newInterval={newInterval}")
                print(f"   Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"❌ intervals={intervals}, newInterval={newInterval} -> Error: {e}")
