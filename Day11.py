from collections import Counter

with open ("input.txt") as f:
    lines = f.read().strip().split(" ")

stones = dict(Counter(lines))


for i in range(75):
    x = {}
    for j in stones:
        if j == "0":
            if "1" in x:
                x["1"] += stones[j]
            else:
                x["1"] = stones[j]
        elif len(j)%2 == 0:
            if j[0:int(len(j)/2)] in x:
                x[str(j[0:int(len(j)/2)])] += stones[j]
            else:
                x[str(j[0:int(len(j)/2)])] = stones[j]
            if str(int(j[int(len(j)/2):])) in x:
                x[str(int(j[int(len(j)/2):]))] += stones[j]
            else:
                x[str(int(j[int(len(j)/2):]))] = stones[j]
        else:
            if str(int(j)*2024) in x:
                x[str(int(j)*2024)] += stones[j]
            else:
                x[str(int(j)*2024)] = stones[j]
    stones = x

sum = 0 
for i in stones:
    sum += stones[i]

print(stones)
print(sum)
        