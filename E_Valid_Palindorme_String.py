#s = "Was it a car or a cat I saw?"
s="0P"
s = s.lower()
print(s)

#Aset = {'a','b','c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

pal = ''

for i in range(len(s)):
    #print(s[i])
    if s[i].isalnum():
        pal += s[i]
    else:
        continue

if pal == pal[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')  # The whole above block can be replaced by return pal = pal[::-1]