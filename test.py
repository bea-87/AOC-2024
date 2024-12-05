import numpy as np
from scipy.ndimage import rotate

# Define the list of lists
lines = [["g", "j", "k"], ["l", "h", "w"], ["r", "t", "t"]]

# Convert to a NumPy array
array = np.array(lines)

# Rotate by 90 degrees counterclockwise using numpy's rot90 function
rotated_array = np.rot90(array, k=1)

# Print the rotated array
print(rotated_array)

