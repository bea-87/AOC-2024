safeValues = 0

def isSafe(nums):
    isAscending = 1 if int(nums[1]) - int(nums[0]) > 0 else -1
    for i in range(len(nums)-1):
        if not ((isAscending*3) >= int(nums[i+1]) - int(nums[i]) >= isAscending or (isAscending*3) <= int(nums[i+1]) - int(nums[i]) <= isAscending) :
            return (0, i)
    return (1, 0)

#Part 1
with open('bob.txt') as f:
    for line in f:
        nums = line.split(" ")
        safeValues += isSafe(nums)[0]

print(safeValues)

#Part 2
with open('bob.txt') as f:
    for line in f:
        nums = line.split(" ")
        if isSafe(nums)[0]:
            safeValues += 1
        else:
            indexNotSafe = isSafe(nums)[1]
            if (isSafe(nums[:indexNotSafe] + nums[indexNotSafe+1:])[0]) or (isSafe((nums[:indexNotSafe+1] + nums[indexNotSafe+2:]))[0]) or (isSafe((nums[:indexNotSafe-1] + nums[indexNotSafe:]))[0]):
                safeValues += 1



print("total", safeValues)