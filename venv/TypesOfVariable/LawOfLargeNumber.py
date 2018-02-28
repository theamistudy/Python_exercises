
import numpy as np
from numpy.random import randn


#--- Expexted mean is 66

limit = 50000
sum = 0

for i in randn(limit):
    if(i > -1 and i <1):
        sum = sum + 1

mean = sum / limit
meanPercentage = mean * 100

print("Limit :",limit)
print("Sum :",sum)
print("Mean :", mean)
print("Mean Percentage :", meanPercentage)
