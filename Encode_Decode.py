input = ["neet","code","love","you"]

class EncodeDecode:

    def encode (self, strs: list[str]) -> str:
        endcode = []
        for s in strs:
            endcode.append(str(len(s))+'#'+s)
        return ''.join(endcode)
    
    def decode (self, s: str) -> list[str]:
        decode =[]
        i=0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            decode.append(s[j+1:j+1+length])
            i =  j + 1 + length
        return decode



encoder = EncodeDecode()

print (encoder.encode(input))
print (encoder.decode(encoder.encode(input)))

# A function inside a class is a method and a method's first parameter is always self
# Methods are called on objects obj.method()