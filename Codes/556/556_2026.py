"""
LeetCode 556: Next Greater Element III
https://leetcode.com/problems/next-greater-element-iii/

Given a positive integer n, find the smallest integer which has exactly the
same digits existing in the integer n and is greater in value than n.
If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a
valid answer but it does not fit in 32-bit integer, return -1.

Example 1:
    Input: n = 12
    Output: 21

Example 2:
    Input: n = 21
    Output: -1

Constraints:
    - 1 <= n <= 2^31 - 1

Hint: Convert n to a list of digits, then apply Next Permutation logic.
     Don't forget to check for 32-bit integer overflow at the end.
"""


from unicodedata import digit


def nextGreaterElement(n: int) -> int:
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    digits = digits[::-1]
    n_digit = len(digits)
    for i in range(n_digit - 2, -1, -1):
        if digits[i] < digits[i+1]:
            for j in range(n_digit - 1, i, -1):
                if digits[i] < digits[j]:
                    digits[i], digits[j] = digits[j], digits[i]
                    digits[i+1:] = reversed(digits[i+1:])
                    result = int("".join(map(str, digits)))
                    if result > 2**31 - 1:
                        return -1
                    else:
                        return result
    return -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "n": 12,
            "expected": 21,
            "description": "Simple swap",
        },
        {
            "n": 21,
            "expected": -1,
            "description": "Already largest permutation",
        },
        {
            "n": 230241,
            "expected": 230412,
            "description": "Multi-digit case",
        },
        {
            "n": 2147483486,
            "expected": -1,
            "description": "Result overflows 32-bit integer",
        },
        {
            "n": 1999999999,
            "expected": -1,
            "description": "Result overflows 32-bit integer",
        },
        {
            "n": 1234,
            "expected": 1243,
            "description": "Swap last two digits",
        },
    ]

    print("=" * 60)
    print("LeetCode 556: Next Greater Element III - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = nextGreaterElement(test["n"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       n={test['n']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")
