import numpy as np

firstArray = np.arange(10)

#Not the way
#splitArray = np.split(firstArray, 2)

splitArray = firstArray.reshape( 2, -1)
print(splitArray)