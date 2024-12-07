import time
start_time = time.time()

result = 0

def checkValidity(total, nums):
    if total == 0 and len(nums) == 0:
        return True
    if len(nums) == 0:
        return False
    if total%nums[-1] == 0:
        if checkValidity(int(total/nums[-1]), nums[:-1]):
            return True
    if total >= nums[-1]:
        if checkValidity(total - nums[-1], nums[:-1]):
            return True
    #Part 2
    if len(str(total)) >= len(str(nums[-1])) and str(total)[-len(str(nums[-1])):] == str(nums[-1]):
        if checkValidity(int(str(total)[:-len(str(nums[-1]))]), nums[:-1]):
            return True
    return False

with open('input.txt') as f:
    for line in f:
        x = line.strip().split(":")
        total = int(x[0])
        nums = [int(a) for a in x[1].split(" ")[1:]]
        if checkValidity(total, nums):
            result += total
            
print(result)

print("--- %s seconds ---" % (time.time() - start_time))
