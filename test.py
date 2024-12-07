import numpy as np
from scipy.ndimage import rotate

lines = [["g", "j", "k"], ["l", "h", "w"], ["r", "t", "t"]]
totalAtm = 20
nums = [12, 3, 4, 5]

print(int("".join([str(totalAtm), str(nums[0])])), nums[1:])

