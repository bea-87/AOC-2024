with open('bob.txt') as f:
   lines = f.read().split('\n')

sum = 0

'''for i in range(len(lines)):
   for j in range(len(lines[i])):
        if lines[i][j] == "X":
            try:
                if lines[i][j+1] + lines[i][j+2] + lines[i][j+3]== "MAS" and j+3 < len(lines[i]):
                    sum += 1
                    print(i, j, 0)
            except:
                print("")
            try:
                if lines[i][j-1] + lines[i][j-2] + lines[i][j-3]== "MAS" and j-3 >= 0:
                    sum += 1
                    print(i, j, 1)
            except:
                print("")
            try:
                if lines[i+1][j] + lines[i+2][j] + lines[i+3][j] == "MAS" and i+3 < len(lines):
                    sum += 1
                    print(i, j, 2)
            except:
                print("")
            try:
                if lines[i-1][j] + lines[i-2][j] + lines[i-3][j] == "MAS" and i-3 >= 0:
                    sum += 1
                    print(i, j, 3)
            except:
                print("")
            try:
                if lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]== "MAS" and j+3 < len(lines[i]) and i+3 < len(lines):
                    sum += 1
                    print(i, j, 4)
            except:
                print("")
            try:
                if lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3]== "MAS" and j-3 >= 0 and i+3 < len(lines):
                    sum += 1
                    print(i, j, 5)
            except:
                print("")
            try:
                if lines[i-1][j+1] + lines[i-2][j+2] + lines[i-3][j+3]== "MAS" and j+3 < len(lines[i]) and i-3 >= 0:
                    sum += 1
                    print(i, j, 6)
            except:
                print("")
            try:
                if lines[i-1][j-1] + lines[i-2][j-2] + lines[i-3][j-3]== "MAS" and j-3 >= 0 and i-3 >= 0:
                    sum += 1
                    print(i, j, 7)
            except:
                print("")'''

for i in range(1, len(lines)-1):
   for j in range(1, len(lines[i])-1):
        if lines[i][j] == "A":
            try:
                if ((lines[i-1][j-1] == "M" and lines[i+1][j+1] == "S") or (lines[i-1][j-1] == "S" and lines[i+1][j+1] == "M")) and ((lines[i-1][j+1] == "M" and lines[i+1][j-1] == "S") or (lines[i-1][j+1] == "S" and lines[i+1][j-1] == "M")):
                    sum += 1
            except:
                print()
print(sum)