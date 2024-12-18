import math

with open('input.txt') as f:
    lines = f.read().strip().split('\n')

A = int(lines[0][12:]) 
B = int(lines[1][12:])
BReset = B
C = int(lines[2][12:])
CReset = C

program = list(int(a) for a in lines[-1][9:].split(","))
pointer = 0
output = []

def performOperation(opcode, operand):
    global A, B, C, pointer
    match opcode:
        case 0:
            A = int(A/(2**([0, 1, 2, 3, A, B, C][operand])))
        case 1:
            B = bitwiseXOR(B, operand)
        case 2:
            B = ([0, 1, 2, 3, A, B, C][operand]) % 8
        case 3:
            if A != 0:
                pointer = operand - 2
        case 4:
            B = bitwiseXOR(B, C)
        case 5:
            output.append(([0, 1, 2, 3, A, B, C][operand]) % 8)
        case 6:
            B = int(A/(2**([0, 1, 2, 3, A, B, C][operand])))
        case 7:
            C = int(A/(2**([0, 1, 2, 3, A, B, C][operand])))

def bitwiseXOR(num1, num2):
    length = max(math.floor((math.log2(num1)) if num1 > 0 else 0) + 1, (math.floor(math.log2(num2)) if num2 > 0 else 0) + 1)
    num1, num2 = f'{num1:0{length}b}', f'{num2:0{length}b}'
    str = ""
    for i in range(length):
        str = str + "0" if num1[i] == num2[i] else str + "1"
    return int(str, 2)

#Part 1
'''while pointer < len(program) - 1:
    performOperation(program[pointer], program[pointer+1])
    pointer += 2

print(",".join(map(str, output)))'''

#Part 2
aPossibilities = [0]
x = 0

for j in range(len(program)):
    x += 1
    oldAPossibilities = aPossibilities
    aPossibilities = []
    for k in oldAPossibilities:
        for i in range(8):
            B, C, pointer, output = BReset, CReset, 0, []
            A = k*8+i
            while pointer < len(program) - 1:
                performOperation(program[pointer], program[pointer+1])
                pointer += 2
            if output[-x] == program[-x]:
                aPossibilities.append(k*8+i)

print(min(aPossibilities))
