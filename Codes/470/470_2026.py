"""
LeetCode 470: Implement Rand10() Using Rand7()
https://leetcode.com/problems/implement-rand10-using-rand7/

Given the API rand7() that generates a uniform random integer in the range [1, 7],
write a function rand10() that generates a uniform random integer in the range [1, 10].
You can only call the API rand7(), and you shouldn't call any other API.

Please do not use the system's Math.random().

Example 1:
    Input: n = 1
    Output: [2]

Example 2:
    Input: n = 2
    Output: [2, 8]

Example 3:
    Input: n = 3
    Output: [3, 8, 10]

Constraints:
    - 1 <= n <= 10^5

Follow up:
    - What is the expected value for the number of calls to rand7() per call to rand10()?
    - Could you minimize the number of calls to rand7()?

Hints:
    - What if you could generate a random number in range [1, 49]? (7 * 7 = 49)
    - (rand7() - 1) * 7 + rand7() gives a uniform distribution over [1, 49].
    - How do you get a uniform [1, 10] from [1, 49]?
    - Think about "rejection sampling": use only the values [1, 40] and reject [41, 49].
    - 40 is the largest multiple of 10 that is <= 49.
"""
import random


# This is the provided API (do not modify)
def rand7():
    return random.randint(1, 7)


def rand10() -> int:
    while True:
        val = (rand7() - 1) * 7 + rand7()
        if val <= 40:
            return val % 10 + 1
        else: # [41, 49]
            val = val - 40 # [1, 9] turning to rand9()
            val = (val - 1) * 7 + rand7() # [1, 63]
            if val <= 60:
                return val % 10 + 1
            else: # [61, 63]
                val = val - 60 # [1, 3]
                val = (val - 1) * 7 + rand7() # [1, 21]
                if val <= 20:
                    return val % 10 + 1
                else:
                    val = val - 20 # [1]
                    val = (val - 1) * 7 + rand7() # [1, 7]
                    continue 




# Test: verify uniform distribution
if __name__ == "__main__":
    # Run rand10() many times and check distribution
    N = 100000
    counts = [0] * 11  # index 1..10

    for _ in range(N):
        val = rand10()
        if 1 <= val <= 10:
            counts[val] += 1
        else:
            print(f"❌ Out of range value: {val}")
            break

    print("=" * 55)
    print("LeetCode 470: Rand10 Distribution Test")
    print(f"Total samples: {N}")
    print("=" * 55)

    expected_pct = 10.0  # each number should appear ~10%
    all_ok = True
    for i in range(1, 11):
        pct = counts[i] / N * 100
        deviation = abs(pct - expected_pct)
        status = "✅" if deviation < 1.5 else "⚠️ "
        if deviation >= 1.5:
            all_ok = False
        print(f"  {i:2d}: {counts[i]:6d} times  ({pct:.2f}%)  {status}")

    print("=" * 55)
    if all_ok:
        print("🎉 Distribution looks uniform!")
    else:
        print("⚠️  Distribution may be skewed. Check your implementation.")
