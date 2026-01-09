s = "racecar"
t = "carrace"

if sorted(s) == sorted(t):
    print(True)
else:
    print(False)

if set(s) == set(t) and len(s) == len(t):
    print(True)
else:
    print(False)
