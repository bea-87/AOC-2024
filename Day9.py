with open('input.txt') as f:
   lines = f.read().strip()

fileFormat = ""
sum = 0

for i in range(len(lines)):
    fileFormat += chr(int(i/2)+100)*int(lines[i]) if i%2 == 0 else "."*int(lines[i])

#Part 1
# indx = fileFormat.find(".")
# while indx != -1:
#     fileFormat = fileFormat[:-1] if fileFormat[-1] == "." else str(fileFormat[:indx]) + str(fileFormat[-1]) + str(fileFormat[indx+1:-1])
#     indx = fileFormat.find(".")


#Part 2
for i in range(len(lines)-1, 0, -2):
    num = fileFormat.count(chr(int(i/2)+100))
    start = fileFormat.find("."*num)
    startChars = fileFormat.find(chr(int(i/2)+100))
    if startChars > start:   
        if start != -1:
            fileFormat = str(fileFormat[:start]) + chr(int(i/2)+100)*num + str(fileFormat[start+num:startChars]) + "."*num + str(fileFormat[startChars+num:])


for i in range(len(fileFormat)):
    if fileFormat[i] != ".":
        sum += (ord(fileFormat[i])-100)*i

print(sum)