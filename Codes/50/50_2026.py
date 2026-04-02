"""
LeetCode 50: Pow(x, n)
https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000

Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100

Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Constraints:
    - -100.0 < x < 100.0
    - -2^31 <= n <= 2^31 - 1
    - n is an integer
    - Either x is not zero or n > 0.
    - -10^4 <= x^n <= 10^4
"""


def myPow(x: float, n: int) -> float:
    # dp[i] = dp[i//2] * dp[i//2]
    def partialPow(_x, _n, _dp):
        # print(_n)
        if _n == 0:
            return 1.0
        if _n == 1:
            return _x
        if _n in _dp:
            return _dp[_n]
        if _n % 2 == 0:
            value = partialPow(_x, _n // 2, _dp) * partialPow(_x, _n // 2, _dp)
        else:
            value = partialPow(_x, _n // 2, _dp) * partialPow(_x, _n // 2, _dp) * _x
        _dp[_n] = value
        return value
    sign = 1 if n >= 0 else 0
    n = abs(n)
    # dp = [-1] * (n + 1)
    dp = {}
    if sign:
        return partialPow(x, n, dp)
    else:
        return 1 / partialPow(x, n, dp)


def myPow_wo_dp(x, n):
    if n == 1:
        return x
    if n == 0 or x == 0:
        return 1
    if n % 2 == 0:
        return myPow_wo_dp(x, n // 2) * myPow_wo_dp(x, n // 2)
    else:
        return myPow_wo_dp(x, n // 2) * myPow_wo_dp(x, n // 2) * x


def myPow_efficiency(x, n):
    if n == 1:
        return x
    if n == 0 or x == 0:
        return 1
    value = myPow_efficiency(x, n // 2)
    if n % 2 == 1:
        return value * value * x
    else:
        return value * value



# Test cases
if __name__ == "__main__":
    test_cases = [
        {"x": 2.00000, "n": 10, "expected": 1024.00000, "description": "2^10"},
        {"x": 2.10000, "n": 3, "expected": 9.261000000000001, "description": "2.1^3"},
        {"x": 2.00000, "n": -2, "expected": 0.25, "description": "2^-2 = 0.25"},
        {"x": 2.00000, "n": 0, "expected": 1.0, "description": "Any number^0 = 1"},
        # {"x": 0.00001, "n": 2147483647, "expected": 0.0, "description": "Very small base, huge exponent"},
        # {"x": 1.00000, "n": -2147483648, "expected": 1.0, "description": "1^n = 1 always"},
        # {"x": -1.00000, "n": -2147483648, "expected": 1.0, "description": "(-1)^even = 1"},
    ]

    print("=" * 65)
    print("LeetCode 50: Pow(x, n) - Test Results")
    print("=" * 65)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = myPow(test["x"], test["n"])
        is_pass = abs(result - test["expected"]) < 1e-5
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       x={test['x']}, n={test['n']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 65)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 65)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")
