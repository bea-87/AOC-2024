from collections import deque

with open('input.txt') as f:
    lines = f.read().strip().split('\n')

numOfRows = len(lines)
numOfCols = len(lines[0])

visited = {}

startPos = (numOfRows - 2, 1)
endPos = (1, numOfCols - 2)
dirList = [(-1, 0), (0, 1), (1, 0), (0, -1)]
minScore = float('inf')
placesToSit = []


#Part 1
toMove = deque([(startPos, 1, 0)])  

def move(curPos, dirIndex, score):
    global minScore
    state_key = (curPos, dirIndex)
    if state_key not in visited or visited[state_key] > score:
        visited[state_key] = score
        if curPos == endPos:
            minScore = min(minScore, score)
        elif score < minScore:
            if lines[curPos[0] + dirList[dirIndex][0]][curPos[1] + dirList[dirIndex][1]] != "#":
                toMove.append(((curPos[0] + dirList[dirIndex][0], curPos[1] + dirList[dirIndex][1]), dirIndex, score + 1))
            toMove.append((curPos, (dirIndex - 1) % 4, score + 1000))
            toMove.append((curPos, (dirIndex + 1) % 4, score + 1000))

while toMove:
    curPos, dirIndex, score = toMove.popleft()
    move(curPos, dirIndex, score)

print(minScore)

#Part 2
toMove = deque([(startPos, 1, 0, [])])  

def move(curPos, dirIndex, score, originalRoute):
    global minScore
    state_key = (curPos, dirIndex)
    if state_key not in visited or visited[state_key] >= score:
        visited[state_key] = score
        routeTaken = list(originalRoute)
        if curPos not in routeTaken:
            routeTaken.append(curPos)
        if curPos == endPos and score == minScore:
            placesToSit.extend(x for x in routeTaken if x not in placesToSit)
        elif score < minScore:
            if lines[curPos[0] + dirList[dirIndex][0]][curPos[1] + dirList[dirIndex][1]] != "#":
                toMove.append(((curPos[0] + dirList[dirIndex][0], curPos[1] + dirList[dirIndex][1]), dirIndex, score + 1, routeTaken))
            toMove.append((curPos, (dirIndex - 1) % 4, score + 1000, routeTaken))
            toMove.append((curPos, (dirIndex + 1) % 4, score + 1000, routeTaken))

while toMove:
    curPos, dirIndex, score, originalRoute = toMove.popleft()
    move(curPos, dirIndex, score, originalRoute)

print(len(placesToSit))
