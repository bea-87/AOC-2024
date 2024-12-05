import re

inpt = '\n'.join(open("input.txt").readlines())
sum = 0
enabled = True

mul = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
do = re.compile(r'do\(\)')
dont = re.compile(r"don't\(\)")
instructions = re.split(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', inpt)

#Part 1
'''mul_matches = mul.findall(inpt)
for match in mul_matches:
    nums = match[4:-1].split(",")
    sum += int(nums[0]) * int(nums[1])'''

#Part 2
for instruction in instructions:
    if mul.match(instruction) and enabled:
        nums = instruction[4:-1].split(",")
        sum += int(nums[0]) * int(nums[1])
    elif do.match(instruction):
        enabled = True
    elif dont.match(instruction):
        enabled = False

print(sum)