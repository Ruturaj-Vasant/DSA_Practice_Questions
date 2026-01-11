#You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. 

# Example 1:

# Input: 
# prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: 
prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0. 

#--------------------------------
# for loop approach O(n^2) time complexity
def maxprofitforloop(prices: list[int])-> int:
    maxP = 0

    for i in range(len(prices)): #O(n)
        for j in range(i+1,len(prices)): #O(n)
            if prices[j] > prices[i]:
                profit = prices[j]-prices[i]
                maxP = max (profit,maxP)

    return maxP

#Time complexity : O(n^2)
#Space complexity : O(1)


#--------------------------------
# two pointer approach O(n) time complexity

def maxprofit(prices: list[int])-> int:

    l , r = 0 , 1
    maxP = 0
    
    while r != len(prices):

        if prices[l]< prices[r]:
            profit = prices[r]-prices[l]
            maxP= max(profit,maxP)
        else:
            l=r

        r +=1

    return maxP

#Time complexity : O(n)
#Space complexity : O(1)

if __name__ == "__main__":
    # print(maxprofit(prices))
    print(maxprofitforloop(prices))