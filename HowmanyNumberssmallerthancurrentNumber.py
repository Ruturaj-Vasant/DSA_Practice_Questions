nums = [8,1,2,2,3]

output = []
# Method 1

# for i in range(len(nums)):
#     count = 0
#     for j in range(len(nums)):
#         if nums[i] > nums[j]:
#             count += 1
#     output.append(count)


# print(output)

# Time complexity if n^2 as we use two loops
# Method 2
temp = sorted(nums)

dictionary={}

for i, num in enumerate(temp):
    print(i,num)
    if num not in dictionary:
        dictionary[num] = i

print(dictionary)

for i in nums:
    output.append(dictionary[i])

print(output)

# Method 3

output_new = [temp.index(i) for i in nums]
print(output_new)