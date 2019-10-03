## Description

## Idea
The problem is partitioned into subproblem as: 

> `dp[i][j]` measures given piles from $i$ to $j$ (included), how many **more** scores can the **first player** gets.  

Therefore, the transition function should be either the first player take `piles[i]` or `piles[j]`, then it turns to the second player as first player:

> `dp[i][j] = max{piles[i] - dp[i+1][j], piles[j] - dp[i][j-1]}`

But I think the most difficult part is how to iterate all the elements in `dp`. The idea is followed:

> `dp[i][i]` is started, with `i` fixed and `j` keep expanding:
> ```python3
> for i in range(n):
> 	for l in range(2, n-i):
> 		j = i + l - 1
> 		dp[i][j] = max(piles[i] - dp[i+1][j], 
> 						piles[j] - dp[i][j-1])
> ```

Here is how to better understand this process: `dp[0][1]` and `dp[0][2]` is taken as example:
> `dp[0][1] = max(piles[0] - dp[1][1], piles[1] - dp[0][0]`

As we have already assigned all the `dp[i][i]`, this work.

Similar applies to `dp[0][2]`