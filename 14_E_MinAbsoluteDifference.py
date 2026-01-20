# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
 

# Example 1:

# Input: 
# arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
# Example 2:

# Input: 
arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]

#-------------------------------------------------
# My Solution

def minAbsoluteDiff(arr: list[int])-> list[list[int]]:

    output = []
    min_diff = float("inf")

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diff = abs(arr[i] - arr[j])
            min_diff = min(min_diff,diff)

    print(min_diff)


    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) == min_diff:
                pair = [arr[i],arr[j]]
                pair.sort()
                output.append(pair)
    output.sort()

    return output

#Total time = O(n^2 + k log k) = worst-case O(n^2 log n)
#O(k) for output

# --------------------------------------------------------
# Optimized Solution similar soluiton but in an optimized manner

def minAbsoluteDiff_optimized(arr: list[int])-> list[list[int]]:
    arr.sort() # sorting is a game chnager helps bring it down from O(n^2 + k log k) to nlogn

    min_diff = float('inf')
    for i in range(1,len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i-1])

    output =[]
    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] == min_diff:
            output.append([arr[i-1],arr[i]])
    return output

if __name__ == "__main__":
    # print(minAbsoluteDiff(arr))
    print(minAbsoluteDiff_optimized(arr))
