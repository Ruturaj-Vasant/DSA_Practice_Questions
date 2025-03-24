# nums=[2,7,11,15]
# target=9

nums=[3,2,4]
target=6

print(len(nums))

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target :
#             print(i,j)
#             break

# The time complexity is n^2
# enumerated array is indexed array, it is assigned an index
# Java Vs Python Intrepreted language?

hash_map ={}

for i,v in enumerate(nums):
    if target-v in hash_map:
        print( i,hash_map[target-v])
    else:
        hash_map[v] = i