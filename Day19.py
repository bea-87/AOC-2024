with open('input.txt') as f:
    lines = f.read().strip().split('\n')

towels = lines[0].split(", ")
patterns = lines[2:]
possibles = []
waysToMake = {}
totalCombos = 0

#Part 1
def createPattern(aim):
    for i in towels:
        if aim == i or (len(aim) >= len(i) and aim[0:len(i)] == i and createPattern(aim[len(i):])):
            return True
    return False

for pattern in patterns:
    if createPattern(pattern):
        possibles.append(pattern)

print(len(possibles))

#Part 2
def countPatterns(aim):
    if aim in waysToMake:
        return waysToMake[aim]
    else:
        numOfWays = 0
        for i in towels:
            if aim == i:
                numOfWays += 1
            elif len(aim) > len(i) and aim[0:len(i)] == i:
                numOfWays += countPatterns(aim[len(i):])
        waysToMake[aim] = numOfWays
        return numOfWays

for i in possibles:
    countPatterns(i)
    totalCombos += waysToMake[i]
print(totalCombos)
