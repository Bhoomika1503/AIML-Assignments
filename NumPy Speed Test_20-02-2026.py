# NumPy Speed Test

import numpy as np
import time

# Python list test
start = time.time()
list_numbers = list(range(1000000))
list_result = [x * 2 for x in list_numbers]
end = time.time()
print("Python List Time:", end - start)

# NumPy array test
start = time.time()
array_numbers = np.arange(1000000)
array_result = array_numbers * 2
end = time.time()
print("NumPy Array Time:", end - start)