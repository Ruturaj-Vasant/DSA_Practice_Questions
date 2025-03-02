# fruits = ['apple' , 'banana', "orange"]

# for index, fruits in enumerate(fruits):
#     print(index,fruits)

# nums = [3, 0, 1]
#nums = [0,1]
nums = [9,6,4,2,3,5,7,0,1]
print(len(nums))

print(len(nums)+1)

print(range(len(nums)+1))

for i in range(len(nums)+1):
    print(i)


print(sum(range(len(nums)+1)))

print(sum(nums))

print(sum(range(len(nums)+1)) - sum(nums))


nums.sort();

print(nums)

def missing_num(nums):
    for index, number in enumerate(nums):
        if index != number:
            return (index)

        if number == len(nums)-1:
            return (number+1)


print (missing_num(nums))
