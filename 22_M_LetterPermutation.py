# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

 

# Example 1:

# Input: 
s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: s = "3z4"
# Output: ["3z4","3Z4"]


def letterpermutation(s):

    output = [""] # we start with an empty string in the output list
    for c in s: # iterate through each character in the input string O(n)
        print(c)
        temp =[]
        if c.isalpha(): # check if the character is an alphabet
            for o in output: # iterate through each string in the output list O(m)
                print("output",o)
                temp.append(o+c.upper()) # append the uppercase version
                temp.append(o+c.lower()) # append the lowercase version
                print("temp",temp)
        else:
            for o in output:
                print("output",o)
                temp.append(o+c)
                print("temp",temp)
        
        output = temp # update output list with the new combinations
    
    return output
# Time Complexity: O(n * 2^m) where n is the length of the string and m is the number of alphabetic characters in the string.
# Space Complexity: O(2^m) for storing the output list.# Explanation:
# For each alphabetic character, we have two choices (uppercase or lowercase), leading


if __name__ == "__main__":
    print(letterpermutation(s))