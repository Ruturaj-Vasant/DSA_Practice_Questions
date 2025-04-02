nums = [-1,0,1,2,-1,-4]
nums.sort()

arr =[]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         for k in range(j+1,len(nums)):
#             if nums[i]+nums[j]+nums[k] == 0:
#                 triplet = [nums[i],nums[j],nums[k]]
#                 if triplet not in arr:
#                     arr.append(triplet)
# print(arr)

#Pointer

for i, v in enumerate(nums):
    if i >0 and v ==nums[i-1]:
        continue

    l, r = i+1, len(nums) -1
    while l<r:
        threesums = v + nums[l] + nums[r]
        if threesums < 0:
            l += 1
        elif threesums>0:
            r -=1
        else:
            triplet = [v,nums[l],nums[r]]
            arr.append(triplet)
            l += 1
            while nums[l]==nums[l-1] and l<r:
                l += 1

print(arr)