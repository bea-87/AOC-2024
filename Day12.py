with open ("input.txt") as f:
    lines = f.read().strip().split("\n")

areas = []
perimeters = []
sides = []
visited = []
numOfRows = len(lines)
numOfCols = len(lines[0])

def findTotalRegion(curRegion, spot, letter):
    newRegion = list(curRegion)
    if lines[spot[0]][spot[1]] == letter:
        newRegion.append(spot)
        visited.append((spot[0], spot[1]))
        if (spot[0] +1, spot[1]) not in visited and spot[0]+1 < numOfRows:
            newRegion = findTotalRegion(newRegion, (spot[0] + 1, spot[1]), letter)
        if (spot[0] -1, spot[1]) not in visited and spot[0]-1 >= 0:
            newRegion = findTotalRegion(newRegion, (spot[0] - 1, spot[1]), letter)
        if (spot[0], spot[1]+1) not in visited and spot[1]+1 < numOfCols:
            newRegion = findTotalRegion(newRegion, (spot[0], spot[1]+1), letter)
        if (spot[0], spot[1]-1) not in visited and spot[1]-1 >= 0:
            newRegion = findTotalRegion(newRegion, (spot[0], spot[1]-1), letter)
    return newRegion

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
    for i in locations:
        x, y = i
        orthogonal = ((x-1, y), (x, y+1), (x+1, y), (x, y-1))
        diagonals = {(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)}
        orthogonalInLocations = set(orthogonal) & locations
        diagonalsNotInLocations = diagonals - locations
        if len(orthogonalInLocations) == 2 and ((orthogonal[0] in orthogonalInLocations) != (orthogonal[2] in orthogonalInLocations)):
            sides += 1
        elif len(orthogonalInLocations) == 1:
            sides += 2
        elif len(orthogonalInLocations) == 0:
            sides += 4
        for j in diagonalsNotInLocations:
            if (j[0], y) in orthogonalInLocations and (x, j[1]) in orthogonalInLocations:
                sides +=1
    return sides

for i in range(numOfRows):
    for j in range(numOfCols):
        if (i, j) not in visited:
            areas.append(set(findTotalRegion([], (i, j), lines[i][j])))
            perimeters.append(findPeri(areas[-1]))
            sides.append(findSides(areas[-1]))

#Part 1
# totPrice = 0
# for i in range(len(areas)):
#     totPrice += len(areas[i])*perimeters[i]
# print(totPrice)

#Part 2
totPrice = 0
for i in range(len(areas)):
    totPrice += len(areas[i])*sides[i]
print(totPrice)
