similarityScore = 0
lOne = []
lTwo = []

#Part 1
with open('bob.txt') as f:
    for line in f:
        x = line.strip().split("   ")
        lOne.append(int(x[0]))
        lTwo.append(int(x[1]))

    lOne.sort()
    lTwo.sort()

    sum = sum(abs(a - b) for a, b in zip(lOne, lTwo))

print(sum)

#Part 2
with open('bob.txt') as f:
    for line in f:
        x = line.strip().split("   ")
        lOne.append(int(x[0]))
        lTwo.append(int(x[1]))

for i in lOne:
    similarityScore += lTwo.count(i) * i

print(similarityScore)
