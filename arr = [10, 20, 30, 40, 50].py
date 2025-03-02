arr = [10, 20, 30, 40, 50]
print(arr)
index = 2
value = 25
arr = arr[:index]+ [value] + arr[index:]
print(arr)
arr = arr[:index] + arr[index + 1:]
print(arr)