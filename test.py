import numpy as np
from scipy.ndimage import rotate

lines = [["g", "j", "k"], ["l", "h", "w"], ["r", "t", "t"]]
total = 2052
nums = [12, 3, 4, 52]

print(int(str(total)[:-len(str(nums[-1]))]))

