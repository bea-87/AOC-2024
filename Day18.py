from collections import deque

with open('input.txt') as f:
    originalLines = f.read().strip().split('\n')

gridSize = 70
fallenBytes = 1024
lines = {tuple(map(int, line.split(','))) for line in originalLines[:fallenBytes]}
visited = {}
toMove = deque([((0, 0), 0)])

def move(pos, score):
    if pos == (gridSize, gridSize):
        return score
    if pos not in visited or visited[pos] > score:
        visited[pos] = score
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_pos = (pos[0] + dx, pos[1] + dy)
            if 0 <= next_pos[0] <= gridSize and 0 <= next_pos[1] <= gridSize and next_pos not in lines:
                toMove.append((next_pos, score + 1))
    return 0

#Part 1
result = 0
while toMove:
    pos, score = toMove.popleft()
    result = move(pos, score)
    if result:
        break

print(result)

#Part 2
for i in range(fallenBytes, len(originalLines)):
    lines.add(tuple(map(int, originalLines[i].split(','))))
    toMove = deque([((0, 0), 0)])
    visited = {}
    result = 0
    while toMove:
        pos, score = toMove.popleft()
        result = move(pos, score)
        if result:
            break
    if result == 0:
        print(originalLines[i])
        break
