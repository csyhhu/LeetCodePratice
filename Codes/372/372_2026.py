"""
LeetCode 372: Super Pow
https://leetcode.com/problems/super-pow/

Your task is to calculate a^b % 1337 where a is a positive integer and b is
an extremely large positive integer given in the form of an array.

Example 1:
    Input: a = 2, b = [3]
    Output: 8

Example 2:
    Input: a = 2, b = [1, 0]
    Output: 1024

Example 3:
    Input: a = 1, b = [4, 3, 3, 8, 8, 3, 2]
    Output: 1

Example 4:
    Input: a = 2147483647, b = [2, 0, 0]
    Output: 1198

Constraints:
    - 1 <= a <= 2^31 - 1
    - 1 <= b.length <= 2000
    - 0 <= b[i] <= 9
    - b does not contain leading zeros.

Hints:
    - Key math property: (a * b) % mod == ((a % mod) * (b % mod)) % mod
    - Decompose the exponent digit by digit from left to right:
        a^[d1, d2, d3] = (a^[d1, d2])^10 * a^d3
    - Use fast power (binary exponentiation) to compute powmod(base, exp, mod).
    - For each new digit: result = powmod(result, 10, mod) * powmod(a, digit, mod) % mod
"""
from typing import List


def superPow(a: int, b: List[int]) -> int:
    result = 1
    for digit in b:
        result = (result ** 10) % 1337 * (a ** digit) % 1337
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        {"a": 2,          "b": [3],                "expected": 8,    "description": "2^3 = 8"},
        {"a": 2,          "b": [1, 0],             "expected": 1024, "description": "2^10 = 1024"},
        {"a": 1,          "b": [4, 3, 3, 8, 8, 3, 2], "expected": 1, "description": "1^anything = 1"},
        {"a": 2147483647, "b": [2, 0, 0],          "expected": 1198, "description": "Large a, b=200"},
        {"a": 2,          "b": [0],                "expected": 1,    "description": "a^0 = 1"},
        {"a": 2,          "b": [1],                "expected": 2,    "description": "a^1 = a % 1337"},
        {"a": 1337,       "b": [1],                "expected": 0,    "description": "1337 % 1337 = 0"},
    ]

    print("=" * 65)
    print("LeetCode 372: Super Pow - Test Results")
    print("=" * 65)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = superPow(test["a"], test["b"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       a={test['a']}, b={test['b']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 65)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 65)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")
