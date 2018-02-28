
import numpy as np


l = [23245,27,546,215,-1234]
print(l)

a = np.array(l)  #--- Difference between arry and list is ---Array contains same data type.
print(a)


# b = np.array(12, 45.5, True, "abc") -- This will results error


print(l.pop())
print(l)

print(a.mean())