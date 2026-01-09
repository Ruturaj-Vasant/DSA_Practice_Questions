timestamps = [0, 100, 200, 900, 950, 1000]
limit = 3

recent= []

for t in timestamps:
    print(t)

count = 0
for prev in recent:
    if t - prev <= 1000:
        count += 1

print("Request in last second:", count)

if count < limit:
    recent.append(t)
    print("Request accepted")
else:
    print("Request denied")