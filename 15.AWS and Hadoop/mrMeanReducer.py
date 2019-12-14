##!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from numpy import mat, mean, power

def read_input(file):
    for line in file:
        yield line.strip()
        
input = read_input(sys.stdin)
mapperOut = [line.split('\t') for line in input]
cumVal, cumSumSq, cumN = 0.0, 0.0, 0.0
for instance in mapperOut[:-1]:
    nj = 100#float(instance[0])
    cumN += nj
    cumVal += nj * float(instance[1])
    cumSumSq += nj * float(instance[2])
mean = cumVal / cumN
varSum = (cumSumSq - 2 * mean *cumVal + cumN * mean * mean) / cumN
print("%d\t%f\t%f" % (cumN, mean, varSum))
print("report: still alive", sys.stderr)


# In[ ]:




