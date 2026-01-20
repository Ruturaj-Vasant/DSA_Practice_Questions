# 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 
# Example 1:

# Input: 
nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]



#------------------------------------------------------------------
# Shallow Copy and Deep Copy
# ✅ shallow = output is NOT a copy

# It just creates a new reference (alias) to the same list.

# output = [1,2,3,4]
# shallow = output

# shallow.append(99)
# print(output)   # [1,2,3,4,99]  ← changed!

# So both variables point to the same list in memory.

# ⸻

# ✅ Shallow copy

# A shallow copy creates a new outer list, but inner objects are shared.

# output = [1,2,3,4]
# shallow = output[:]   # or output.copy()

# Now:

# shallow.append(99)
# print(output)   # unchanged

# ✅ Works for 1D lists.

# ⸻

# ✅ Deep copy

# A deep copy creates a new list and also copies all nested objects inside.

# Example:

# import copy
# output = [[1,2], [3,4]]
# deep = copy.deepcopy(output)

# Now modifying inside won’t affect original:

# deep[0].append(99)
# print(output)   # [[1,2], [3,4]] unchanged


# ⸻

# Key difference
# 	•	Shallow copy: copies outer container only
# 	•	Deep copy: copies everything recursively

# ⸻

# One-line answer

# You can’t do shallow = output because that is not copying, it’s just two names for the same list.

def subset_backtrack(nums):
    
    def backtrack(start, path): # start is the index to start from, path is the current subset being built
        output.append(path[:]) # append a copy of the current path to output why do we need to append a copy? because path is mutable and will change in future calls

        for i in range(start, len(nums)): # why iterate through the numbers starting from 'start' index? because we want to avoid duplicates and ensure subsets are built in a specific order
            path.append(nums[i]) # include nums[i] in the current subset
            backtrack(i+1,path) # move to the next index to continue building the subset 

            path.pop() # backtrack: remove the last added element to explore other subsetsß

    
    output =[] # list to store all subsets
    backtrack(0,[]) # start backtracking from index 0 with an empty path
    return output 


def subset(nums):
    output = [[]]  # start with the empty subset

    for num in nums:  # iterate through each number in the input list
        print("we are iterating on num", num)
        # For each number, add it to all existing subsets to create new subsets
        # new_subsets = [curr + [num] for curr in output]
        #simply the above for loop
        print("output before adding new subsets", output)
        new_subsets = []
        for curr in output:
            print("curr", curr)
            new_subsets.append(curr + [num])
            print("new_subsets", new_subsets)

        output += new_subsets  # add the new subsets to the output list
        print("output", output)
        print("==========================")
        print()

    print(output)
    return output
# Time Complexity: O(n * 2^n) where n is the length of nums.
# Space Complexity: O(2^n) for storing all subsets in the output list.# Explanation:
# Each element can either be included or excluded from a subset, leading to 2


if __name__ == "__main__":
    # print(subset(nums))
    print(subset_backtrack(nums))
    