import time
start_time = time.time()

result = 0

def checkValidity(total, totalAtm, nums):
    if total == totalAtm and len(nums) == 0:
        return True
    if len(nums) == 0 or totalAtm > total:
        return False
    if checkValidity(total, totalAtm*nums[0], nums[1:]):
        return True
    if checkValidity(total, totalAtm+nums[0], nums[1:]):
        return True
    #Part 2
    if checkValidity(total, int("".join([str(totalAtm), str(nums[0])])), nums[1:]):
        return True
    return False

with open('input.txt') as f:
    for line in f:
        x = line.strip().split(":")
        total = int(x[0])
        nums = [int(a) for a in x[1].split(" ")[1:]]
        if checkValidity(total, nums[0], nums[1:]):
            result += total
            
print(result)

print("--- %s seconds ---" % (time.time() - start_time))
