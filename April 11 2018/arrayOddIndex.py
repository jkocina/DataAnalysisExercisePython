import numpy as np

fullArray = np.arange(25)

oddArray = fullArray[fullArray % 2 == 1 ]

print(oddArray)