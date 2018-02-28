

import numpy as np
from numpy.random import randn


print(randn())
print("hello")


#----- If statement -------  -2    -1   0    1    2  ----------

x = randn()

answer = None

if x >1:
    answer = "Greater than 1"

else:
    if  x >= -1:
        answer = "Between -1 and 1"
    else:
        answer = "Less than -1"
print(x)
print(answer)



#----- Chained statement -----------

#----- If statement -------  -2    -1   0    1    2  ----------

x = randn()

answer = None

if x >1:
    answer = "Greater than 1"

elif x >= -1:
    answer = "Between -1 and 1"
else:
    answer = "Less than -1"

print(x)
print(answer)





