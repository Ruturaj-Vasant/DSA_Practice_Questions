# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: 
coins = [1,2,5]
amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0


def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    print(dp)

    for index in range(1, amount+1):
        for coin in coins:
            if coin <= index: # the coin we chose should be smaller or equal in denomination for comparison
                dp[index] = min (dp[index], 1+dp[index - coin]) # here 1+dp[index - coin] means we are adding one coin to the minimum coins required for the remaining amount (index - coin) for example if index is 7 and coin is 5 then we need to find minimum coins for amount 2 (7-5) and add one coin of denomination 5
    print(dp)
    return dp[amount] if (dp[amount] != float('inf')) else -1


if __name__ == "__main__":
    print(coin_change(coins, amount)) 

