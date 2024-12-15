with open ("input.txt") as f:
    lines = f.read().strip().split("\n")

areas = []
perimeters = []
sides = []
visited = []
numOfRows = len(lines)
numOfCols = len(lines[0])

def findTotalRegion(curRegion, spot, letter):
    if lines[spot[0]][spot[1]] == letter:
        curRegion.append(spot)
        visited.append((spot[0], spot[1]))
        if (spot[0] +1, spot[1]) not in visited and spot[0]+1 < numOfRows:
            curRegion = findTotalRegion(curRegion, (spot[0] + 1, spot[1]), letter)
        if (spot[0] -1, spot[1]) not in visited and spot[0]-1 >= 0:
            curRegion = findTotalRegion(curRegion, (spot[0] - 1, spot[1]), letter)
        if (spot[0], spot[1]+1) not in visited and spot[1]+1 < numOfCols:
            curRegion = findTotalRegion(curRegion, (spot[0], spot[1]+1), letter)
        if (spot[0], spot[1]-1) not in visited and spot[1]-1 >= 0:
            curRegion = findTotalRegion(curRegion, (spot[0], spot[1]-1), letter)
    return curRegion

def findPeri(locations):
    peri = 0
    for i in locations:
        if (i[0]+1, i[1]) not in locations:
            peri += 1
        if (i[0]-1, i[1]) not in locations:
            peri += 1
        if (i[0], i[1]+1) not in locations:
            peri += 1
        if (i[0], i[1]-1) not in locations:
            peri += 1
    return peri

def findSides(locations):
    sides = 0

    return sides

for i in range(numOfRows):
    for j in range(numOfCols):
        if (i, j) not in visited:
            areas.append(findTotalRegion([], (i, j), lines[i][j]))
            perimeters.append(findPeri(areas[-1]))
            sides.append(findSides(areas[-1]))

#Part 1
totPrice = 0
for i in range(len(areas)):
    totPrice += len(areas[i])*perimeters[i]
print(totPrice)

#Part 2
totPrice = 0
for i in range(len(areas)):
    totPrice += len(areas[i])*sides[i]

print(totPrice)