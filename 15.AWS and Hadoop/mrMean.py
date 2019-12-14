#!/usr/bin/env python
# coding: utf-8

# In[3]:


from mrjob.job import MRJob

class MRmean(MRJob):
    def __init__(self, *arg, **kwargs):    #*self._args：表示接受元组类参数；**kwargs：表示接受字典类参数；
        super(MRmean, self).__init__(*args, **kwargs)    #调用父类（超类）
        self.inCount = 0
        self.inSum = 0
        self.inSqSum = 0
        
    def map(self, key, val):
        if False: yield
        inVal = float(val)
        self.inCount += 1
        self.inSum += inVal
        self.inSqSum += inVal * inVal
        
    def map_final(self):
        mn = self.inSum / self.inCount
        mnSq = self.inSqSum / self.inCount
        yield(1, [self.inCount, mn, mnSq])
        
    def reduce(self, key, packedValues):
        cumVal, cumSumSq, cumN = 0.0, 0.0, 0.0
        for valArr in packedValues:
            nj = float(valArr[0])
            cumN += nj
            cumVal += nj * float(valArr[1])
            cumSumSq += nj * float(valArr[2])
        mean = cumVal / cumN
        var = (cumSumSq - 2 * mean * cumVal + cumN * mean * mean) / cumN
        yield(mean, var)
        
    def steps(self):
        return ([self.mr(mapper = self.map, reducer = self.reduce, mapper_final = self.map_final)])


# In[ ]:




