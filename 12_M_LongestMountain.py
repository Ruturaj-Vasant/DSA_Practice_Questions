# Question: Given an array arr of integers, return the length of the longest mountain in arr.
# If there is no mountain, return 0.
# Example 1:
# Input: 
arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The longest mountain is [1,4,7,3,2] which has length 5.
# Example 2:
# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.

def find_mountain(arr:list[int])->int:


    largest_moutain = 0
    # for i , v in enumerate(arr):
        
    #     if i == 0 and i == len(arr)-1:
    #         print("skipping first and last index")
    #         continue 
    # The whole above block can we written as below

    for i in range(1, len(arr)-1):
        
        # print(l,r)
        if arr[i-1]<arr[i]>arr[i+1]:
            l=r=i
            print("peak:", arr[i-1],arr[i],arr[i+1])
            # while l > 0:
            #     print("inside L loop")
            #     if arr[l]>arr[l-1]:
            #         l -= 1
            #     else:
            #         break
            # The whole above block can be written as
            while l>= 0 and arr[l] > arr[l-1]:
                l -= 1
            # while r<len(arr)-1:
            #     print("inside R loop")
            #     if arr[r]>arr[r+1]:
            #         r += 1
            #     else:
            #         break
            # The whole above block can be written as
            while r <=len(arr)-1 and arr[r] > arr[r+1]:
                r += 1

            largest_moutain = max(largest_moutain,r-l+1)
    
    return largest_moutain


if __name__ == "__main__":

    print(find_mountain(arr))