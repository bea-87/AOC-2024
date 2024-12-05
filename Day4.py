import numpy as np
from scipy.ndimage import rotate
with open('input.txt') as f:
   lines = f.read().split('\n')

sum = 0 

#Part 1
for i in range(len(lines)):
    lines[i] = list(lines[i])
lines = np.array(lines)

def countDiagonals(lines):
    count = 0
    for i in range(len(lines)-3):
        for j in range(len(lines)-3):
                if lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]== "XMAS":
                    count += 1
    return count

for p in range(4):
    print(sum)
    for j in lines:
        sum += ''.join(j).count("XMAS")
    print(sum)
    sum += countDiagonals(lines)
    lines = np.rot90(lines, k=1)



#Part 2
'''for i in range(1, len(lines)-1):
   for j in range(1, len(lines[i])-1):
        if lines[i][j] == "A":
            if ((lines[i-1][j-1] == "M" and lines[i+1][j+1] == "S") or (lines[i-1][j-1] == "S" and lines[i+1][j+1] == "M")) and ((lines[i-1][j+1] == "M" and lines[i+1][j-1] == "S") or (lines[i-1][j+1] == "S" and lines[i+1][j-1] == "M")):
                sum += 1
'''
print(sum)