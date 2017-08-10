import math
from functools import reduce


class NormD:

    def avrg(self,sl):
        n = len(sl)
        avrg = reduce(lambda a,b :a+b,sl) /n
        return avrg

    def var(self,avrg,sl):
        n = len(sl)
        var = reduce(lambda a,b : a+(b-avrg)**2,sl,0)/n
        return var

    def std_dev(self,var):
        std_dev = round(math.sqrt(var),1)
        return std_dev

    
    
