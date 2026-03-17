"""
[252] Meeting Rooms
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
determine if a person could attend all meetings.

A person is free if there is no overlap between any two meetings. Two meetings
with adjacent times are not overlapping (e.g. [1,2] and [2,3] are adjacent).

Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: false
    Explanation: Person cannot attend all meetings because [0,30] and [5,10] overlap.

Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: true
    Explanation: Person can attend all meetings because [7,10] and [2,4] don't overlap.

Example 3:
    Input: intervals = [[0,5],[5,10]]
    Output: true
    Explanation: [0,5] and [5,10] are adjacent, not overlapping.

Example 4:
    Input: intervals = [[1,4],[2,3]]
    Output: false
    Explanation: [1,4] and [2,3] overlap.

Constraints:
    - 0 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i < end_i <= 10^6

Date: 2026-03-08
"""


def canAttendAllMeetings(intervals):
    """
    Determine if a person can attend all meetings without conflicts.
    
    Args:
        intervals: List of meeting time intervals [start, end]
    
    Returns:
        Boolean indicating if all meetings can be attended
    """
    interval_bucket = [0] * 1000000
    for start, end in intervals:
        if (sum(interval_bucket[start: end])) > 0:
            return False
        else:
            interval_bucket[start: end] = [1] * (end - start)
    return True


def canAttendAllMeetings_Optimal(intervals):
    """
    OPTIMAL SOLUTION - Sorting + Adjacent Comparison
    
    Core Idea:
    -----------
    1. Sort intervals by start time
    2. Check only ADJACENT intervals for conflicts
    3. If no adjacent intervals overlap, no conflicts exist
    
    Why this works:
    ---------------
    After sorting by start time, if intervals[i] doesn't overlap with intervals[i+1],
    then intervals[i] won't conflict with ANY meeting after it (because all future
    meetings have start times >= intervals[i+1].start, which is > intervals[i].end)
    
    Time Complexity: O(n log n) - dominated by sorting
    Space Complexity: O(1) - not counting sort's internal space
    
    Key Overlap Detection:
    ----------------------
    Two intervals [a, b] and [c, d] where a <= c (after sorting):
    - NO overlap: b <= c  (or equivalently: NOT (b > c))
    - OVERLAP:    b > c
    
    Examples:
    ---------
    [0,5] and [5,10]:  5 > 5? False → NO overlap ✓
    [0,6] and [5,10]:  6 > 5? True  → OVERLAP ✗
    [1,4] and [2,3]:   4 > 2? True  → OVERLAP ✗
    
    Edge Cases to Consider:
    -----------------------
    - Empty list: return True (no conflicts)
    - Single meeting: return True (can attend it)
    - Adjacent meetings with same end/start: should NOT conflict
    """
    # Handle edge cases
    if not intervals or len(intervals) == 1:
        return True
    
    # Step 1: Sort intervals by start time
    # After sorting, compare only adjacent meetings
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Check if any two adjacent intervals overlap
    # Loop through and check: does meeting i's end overlap with meeting i+1's start?
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i+1][0]:
            # Conflict found!
            return False
    
    # No conflicts found
    return True


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[0,30],[5,10],[15,20]], False),
        ([[7,10],[2,4]], True),
        ([[0,5],[5,10]], True),
        ([[1,4],[2,3]], False),
        ([], True),
        ([[1,2]], True),
        ([[0,5],[1,6],[2,7],[3,8],[4,9]], False),
        ([[1,10],[2,3],[4,5],[6,7]], False),
        ([[1,3],[3,5],[5,7]], True),
    ]
    
    print("=" * 70)
    print("LeetCode 252 - Meeting Rooms")
    print("=" * 70)
    
    print("\n--- Testing Your Solution (Brute Force with Bucket) ---")
    for intervals, expected in test_cases:
        try:
            # Make a copy since the function modifies it
            result = canAttendAllMeetings(intervals.copy())
            if result is None:
                print(f"⚠️  intervals={intervals} -> Not implemented")
            else:
                is_correct = result == expected
                status = "✓" if is_correct else "✗"
                print(f"{status} intervals={intervals}")
                print(f"   Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"❌ intervals={intervals} -> Error: {e}")
    
    print("\n--- Testing Optimal Solution (Sort + Adjacent Check) ---")
    for intervals, expected in test_cases:
        try:
            # Make a copy since the function modifies it
            result = canAttendAllMeetings_Optimal(intervals.copy())
            if result is None:
                print(f"⚠️  intervals={intervals} -> Not implemented")
            else:
                is_correct = result == expected
                status = "✓" if is_correct else "✗"
                print(f"{status} intervals={intervals}")
                print(f"   Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"❌ intervals={intervals} -> Error: {e}")
