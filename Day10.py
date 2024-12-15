lines = []
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(list(int(a) for a in line))

trailHeads1 = 0
trailHeads2 = 0

numOfRows = len(lines)
numOfCols = len(lines[0])

def findTrails(x, y):
    numOfTrails = 0
    if lines[x][y] == 9:
        if [x, y] not in uniqueVals:
            uniqueVals.append([x, y])
        return 1
    if x + 1 < numOfRows and lines[x+1][y] == lines[x][y] + 1:
        numOfTrails += findTrails(x+1, y)
    if x > 0 and lines[x-1][y] == lines[x][y] + 1:
        numOfTrails += findTrails(x-1, y)
    if y + 1 < numOfRows and lines[x][y+1] == lines[x][y] + 1:
        numOfTrails += findTrails(x, y+1)
    if y > 0 and lines[x][y-1] == lines[x][y] + 1:
        numOfTrails += findTrails(x, y-1)
    return numOfTrails

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 0:
            uniqueVals = []
            trailHeads2 += findTrails(i, j)
            trailHeads1 += len(uniqueVals)

print(trailHeads1, trailHeads2)