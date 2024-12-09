for i in range(len(lines)-1, 0, -2):
    num = fileFormat.count(chr(int(i/2)+100))
    start = fileFormat.find("."*num)
    startChars = fileFormat.find(chr(int(i/2)+100))
    if startChars != start:   
        if start != -1:
            fileFormat = str(fileFormat[:start]) + chr(int(i/2)+100)*num + str(fileFormat[start+num:startChars]) + "."*num + str(fileFormat[startChars+num:])
            for i in range(len(fileFormat)):
                if fileFormat[i] != ".":
                    print((ord(fileFormat[i])-100), end="")
                else:
                    print(".", end="")