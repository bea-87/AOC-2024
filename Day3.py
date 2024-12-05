import re

sum = 0
inpt = '\n'.join(open("bob.txt").readlines())

mul = re.compile(r'mul\(\d?\d?\d,\d?\d?\d\)')
mul = mul.findall(inpt)
for i in mul:
    nums = i[4:-1].split(",")
    sum += int(nums[0])*int(nums[1])

print(sum)