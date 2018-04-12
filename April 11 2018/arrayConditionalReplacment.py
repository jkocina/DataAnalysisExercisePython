import numpy as np

anArray = np.arange(35)

anArray[anArray % 2 == 1] = 0

print(anArray)