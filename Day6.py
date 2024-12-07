with open('input.txt') as f:
   lines = f.read().split('\n')

curPos = [0, 0]
fixedPos = [0, 0]
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
direcIndex = 0

for i in lines:
    for j in i:
        if j == "^":
            curPos = [lines.index(i), i.index(j)]
            fixedPos = curPos
    lines[lines.index(i)] = list(lines[lines.index(i)])

#Part 1
'''while True:
    direc = direction[direcIndex]
    lines[curPos[0]][curPos[1]] = "X"
    if curPos[0]+direc[0] >= len(lines) or curPos[0]+direc[0] < 0 or curPos[1]+direc[1] >= len(lines[0]) or curPos[1]+direc[1] < 0:
        break
    elif lines[curPos[0]+direc[0]][curPos[1]+direc[1]] == "#":
        direcIndex = (direcIndex + 1) % 4
    else:
        curPos = [curPos[0]+direc[0], curPos[1]+direc[1]]

sum = 0
for i in lines:
   sum += i.count("X")'''

#Part 2
sum = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        curPos = fixedPos
        direcIndex = 0
        if lines[i][j] ==  ".":
            sum += 1
            for m in range(7000): #increase value to be sure of accuracy but takes longer to run about 7000 works for my input
                direc = direction[direcIndex]
                if curPos[0]+direc[0] >= len(lines) or curPos[0]+direc[0] < 0 or curPos[1]+direc[1] >= len(lines[0]) or curPos[1]+direc[1] < 0:
                    sum -= 1
                    break
                elif lines[curPos[0]+direc[0]][curPos[1]+direc[1]] == "#" or (curPos[0]+direc[0] == i and curPos[1]+direc[1] == j):
                    direcIndex = (direcIndex + 1) % 4
                else:
                    curPos = [curPos[0]+direc[0], curPos[1]+direc[1]]



print(sum)