from collections import deque

# Question: Given a sorted array of integers, return an array of the squares of each number sorted in non-decreasing order.
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# Explanation: After squaring, the array becomes [49,9,4,9,121].
# After sorting, it becomes [4,9,9,49,121]. 


nums = [-4,-3,0,1,10]

#--------------------------------------------------
# My initial solution
def squared_nums_simple(nums: list[int])->list[int]:

    sq =[]

    for i in nums: #O(n)
        j = i*i
        # print(j)
        sq.append(j)
    
    sq.sort() # O(nlogn)
    return(sq)

    # sq_sorted = [i**2 for i in nums]
    # sq_sorted.sort()

    #above is shorter version of the code
# In the above solution the bottle neck is the sort function with n log n time complexity 


#--------------------------------------------------------------
def two_pointer(nums:list[int])-> list[int]:

    sorted_dqueue = deque()

    l, r = 0, len(nums)-1
    print(l,r)

    while l <= r: # This is a common condition for the pointer to work, it stops from pointer from overlapping. #O(n)
        # left , right = abs(nums[l]), abs(nums[r])

        if abs(nums[l]) > abs(nums[r]): # O(1) This condition works coz the list that we have is already sorted. hence we choose the biggest number from the both ends and keep appending its square from the left. For this logic to work you have to choose the biggest and then append from the left. You cannot choose the smallest from both end coz the smallest square will be somewhere at the middle of the list and not at teh end.
            sorted_dqueue.appendleft(nums[l]**2) # appending from left is important after choosing the biggest absolute number.
            l += 1
        else:
            sorted_dqueue.appendleft(nums[r]**2)
            r -= 1
        # print(sorted_dqueue)
    return list(sorted_dqueue) # converting the dqueue to list as list is expected obj at the end.

if __name__ == "__main__":
    # print(squared_nums_simple(nums))
    print(two_pointer(nums))



