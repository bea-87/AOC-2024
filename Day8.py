import math

with open('input.txt') as f:
   lines = f.read().strip().split('\n')

antinodesPoses = []

numRows = len(lines)
numCols = len(lines[0])

#Part 1
for i in range(numRows):
    for j in range(numCols):
        if lines[i][j] != ".":
            for m in range(i, numRows):
                for n in range(numCols):
                    if lines[i][j] == lines[m][n] and (i != m or j != n):
                        #Part 1
                        '''if 2*m-i < numRows and 2*m - i >= 0 and 2*n-j < numCols and 2*n-j >= 0:
                            if (2*m-i, 2*n-j) not in antinodesPoses:
                                antinodesPoses.append((2*m-i, 2*n-j))
                        if 2*i-m < numRows and 2*i - m >= 0 and 2*j-n < numCols and 2*j-n >= 0:
                            if (2*i-m, 2*j-n) not in antinodesPoses:
                                antinodesPoses.append((2*i-m, 2*j-n))'''
                        
                        #Part 2
                        HCF = math.gcd(i-m, j-n)
                        gradient = [(i-m)/HCF, (j-n)/HCF]
                        for direction in [-1, 1]:
                            start = (i, j)
                            while 0 <= start[0] < numRows and 0 <= start[1] < numCols:
                                if start not in antinodesPoses:
                                    antinodesPoses.append(start)
                                start = (start[0] + direction * gradient[0],start[1] + direction * gradient[1],)
                        start = [i, j]

print(len(antinodesPoses))