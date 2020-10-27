def coinChange_DP(coins, amount):

    MAX = 1E9
    dp = [MAX] * (amount + 1) # dp[i]: Using all coins, the minimal number of coins used to make up i
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i - c] + 1, dp[i])

    if dp[amount] != MAX:
        return dp[amount]
    else:
        return -1


def coinChange(coins, amount):

    coins.sort(reverse = True)

    result = [1e9]

    def dfs(coins, coin_index, remain_amount, count, result: list):

        if remain_amount == 0:
            result[0] = min(result[0], count)
            return

        if coin_index == len(coins):
            return

        this_coin = coins[coin_index]
        max_num_coin = remain_amount // this_coin
        for k in range(max_num_coin, -1, -1):
            if k + count >= result[0]:
                break
            dfs(coins, coin_index + 1, remain_amount - k * this_coin, count + k, result)

    dfs(coins, 0, amount, 0, result)
    if result[0] == 1e9:
        return -1
    else:
        return result[0]

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

coins = [2]
amount = 3
print(coinChange(coins, amount))

coins = [1]
amount = 0
print(coinChange(coins, amount))

coins = [1]
amount = 1
print(coinChange(coins, amount))

coins = [1]
amount = 2
print(coinChange(coins, amount))