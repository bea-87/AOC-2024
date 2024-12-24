with open("input.txt") as f:
    lines = f.read().strip().split('\n')

totalCheats = 0
startPos = ()
endPos = ()
cheatLen = 20 #change this to 2 for part 1 or keep as 20 for part 2

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "S":
            startPos = (i, j)
        elif char == "E":
            endPos = (i, j)

def findNext(curPos, prevPos):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nextPos = (curPos[0] + dx, curPos[1] + dy)
        if nextPos != prevPos and lines[nextPos[0]][nextPos[1]] in ".E":
            return nextPos

curPos = startPos
racePath = [startPos]
prevPos = None

racePath = [startPos, findNext(curPos, curPos)]
curPos = racePath[1]
while curPos != endPos:
    curPos = findNext(curPos, racePath[-2])
    racePath.append(curPos)

racePathIndices = {pos: idx for idx, pos in enumerate(racePath)}
for start in racePath:
    for x in range(-cheatLen, cheatLen + 1):
        for y in range(-cheatLen, cheatLen + 1):
            if abs(x) + abs(y) <= cheatLen:
                cheatEnd = (start[0] + x, start[1] + y)
                if cheatEnd in racePathIndices:
                    if racePathIndices[cheatEnd] - racePathIndices[start] >= 100 + abs(x) + abs(y):
                        totalCheats += 1

print(totalCheats)
