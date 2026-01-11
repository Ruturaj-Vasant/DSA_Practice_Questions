integer = 5 # Integer
float_int = 3.14 #Float

is_okay = (10>5) # boolean
print(is_okay)

name = "Rutu" # String
print(name.upper().lower())


#-------------------------------------
# Lists

list_a = [1,2,3,4,2,3,1] # list is ordered, mutable, allows duplicates Ordered = position matters and is fixed

# Basic operations on lists
list_a.append(5) # adding element to the end of the list
list_a.insert(2, 10) # inserting 10 at index 2
list_a.remove(3) # removing first occurrence of 3 from the list
list_a.pop() # removing and returning the last element of the list
list_a.sort() # sorting the list in ascending order
list_a.reverse() # reversing the list
print(list_a.index(2)) # returns the first index of 2 in the list
print(list_a.count(2)) # counts number of occurrences of 2 in the list
print(len(list_a)) # returns the length of the list
print(list_a[2]) # accessing element at index 2
print(list_a[1:4]) # slicing list from index 1 to 3
print(list_a + [6,7,8]) # concatenating lists
print(list_a * 2) # repeating list


#-------------------------------------
# Tuples

tuple_b = (1,2,3,4,2,3,1) # Tuple os ordered, immutable, allows duplicates. Tuples are slightly faster and use less memory.

#basic operations on tuples
print(tuple_b.count(2)) # counts number of occurrences of 2 in tuple
print(tuple_b.index(3)) # returns the first index of 3 in tuple 
print(len(tuple_b)) # returns the length of the tuple
print(tuple_b[2]) # accessing element at index 2
print(tuple_b[1:4]) # slicing tuple from index 1 to 3
print(tuple_b + (5,6,7)) # concatenating tuples
print(tuple_b * 2) # repeating tuple
# adding or removing elements from tuple is not possible as tuples are immutable


#-------------------------------------
#Sets

set_c = {1,2,3,4,2,3,1} # set is unordered and unique

#Basic Operations on sets
set_c.add(5) # adding element to set
set_c.remove(2) # removing element from set
set_c.add(3) # adding duplicate element to set has no effect
set_c.update([6,7,8]) # adding multiple elements to set
set_c.discard(10) # removing element that is not present in set has no effect

print(set_c)

#-------------------------------------


print(list_a, tuple_b, set_c)

user = {name: "Rutu", "age": 20, "is_student": True} # dictionary is unordered, mutable, key-value pairs


# Hasahable means that the object has a fixed value during its lifetime and can be used as a key in a dictionary or as an element in a set. Immutable objects like strings, tuples, and frozensets are hashable, while mutable objects like lists, sets, and dictionaries are not.

tuple_a = tuple(list_a) # converting list to tuple
set_a = set(list_a) # converting list to set

print(tuple_a)
print(set_a)


#-------------------------------------
# Matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
] # 2D list
for row in matrix: #printing row
    for element in row: # printing element
        print(element, end=" ")
    print()
