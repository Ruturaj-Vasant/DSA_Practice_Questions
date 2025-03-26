digits = [1,2,3]
# exponential is written as ** in python
# adding similar datatypes like string += string, list += list adds two list 
# text = "Hello"
# text += " World"  # text -> "Hello World" 
# nums = [1, 2, 3]
# nums += [4, 5]  # nums -> [1, 2, 3, 4, 5]


# Append Used to add an element to the end of a list
# numbers = [1, 2, 3]
# numbers.append(4)  # numbers -> [1, 2, 3, 4]

# when we have a list we use join words = ["Hello", "World"]
# result = " ".join(words)  # Output: "Hello World"



nums = 1
for i,d in enumerate(digits):
    nums += d * 10 ** (len(digits)-i-1)

arr =[]
for i in str(nums):
    arr.append(int(i)) # adding an element Append
print(arr)



#Smart just add the last digit if it is less than 10 or else set it to 
# zero and repeat it for next int, if the loop never breaks insert 1 at the start
for i in range(len(digits)-1, -1, -1):
    digits[i] += 1
    if digits[i] < 10:
        break
    else:
        digits[i]=0
else:
    digits.insert(0,1)
print(digits)