import numpy as np

anArray = np.arange(35)

out = np.where((anArray % 2 == 1), -1, anArray)

print(out)