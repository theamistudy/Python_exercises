
import numpy as np

list1 = [23245, 27, 65, 546, -1234]
print(list1)

a = np.array(list1)
print(a)
print(a[2:4])   #-- List slicing creates a copy of the list, but array slicing does not.

b = a[2:4]
print(b)
print(b[0])
print(b[:])

b[:] = 111
print(b)
print(a)  #---- Slicing does not create a new array, works on a view of the array

c = a.copy();  #-- Explicit Copy needs to be called to create a copy
print(c)

c[:] = 222
print(c)
print(a)