## Problem Description:

## Idea:
The analysis of the input array is conducted one by one. The latter added element will 
take effect to the previous results. Therefore Greedy will not be possible.

Here dynamic programming is considered.

This problem should be divided into: 

> When a new element is added, to generate the maximum array, we try to assign this 
> value to the previous consecutive k elements, with the summation of the maximum array
> before the changed k elements.

Formally, we define `dp[i]` as the largest sum of the given array after partitioning from `A[0],...,A[i]`. Therefore, `dp[-1]` 
is the desired solution.

`dp[i]` can be divided into the following `k` subproblem as:

- `dp[i-1] + max(A[i])`
- `dp[i-2] + max(A[i-1], A[i])`
- ...
- `dp[i-k] + max(A[i-k+1],...,A[i])`

The largest one above is assigned to `dp[i]`.

The transition function will be:
```python
for k in range(1, K+1):
    dp[i] = max(dp[i], dp[i-k] * k * max(A[i-k-1: i+1]))
```
Here are some concerns:

- In order to incorporate `k` subproblems, we need to have `k` to reach `K`, which 
leads to the `K+1` in the `range`.
- If `i-k < 0`, we ignore the `dp[i-k]`. 
- In order to incorporate `k` elements in `A` to find the maximum value, we need to have
 `i+1` because slicing in `python` doesn't contain the final element.
- Therefore, the outer loop of `i` gets some problem: `for i in range(1, len(A))` is not feasible,
which leads to out of index when we access to `i+1` in `A`. To solve it, I add an extra `0` in `A`
before processing.
- However, after doing all these above the submitted codes still get `Time Limit Exceeded`. I search
online and find one way to reduce the time is to find `max(A[i-k-1: i+1])` more efficiently, here is 
one of the solution:
```python
max_value = float('-inf')
for k in range(1, K + 1):
    max_value = max(max_value, A[i-k+1])
    dp[i] = max(dp[i], dp[i-k] + k * max_value)
```

