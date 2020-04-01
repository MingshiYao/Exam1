# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:53:33 2020

@author: Hasee
"""
import random
import matplotlib.pyplot as plt
import numpy as np
import math
def decayFunc(N,lambd):
    t = 0
    Nwitht=[0]
    DeltaNwitht=[0]
    while N > 0:
        DeltaN = 0
        for i in range(N):
            if (random.random() < lambd):
                DeltaN = DeltaN + 1
        t = t + 1
        N = N - DeltaN
        if (N>0):
            Nwitht[t-1]=math.log(N)
        Nwitht=Nwitht+[0]
        if (DeltaN>0):
            DeltaNwitht[t-1]=math.log(DeltaN)
        DeltaNwitht=DeltaNwitht+[0]
    return t,DeltaNwitht,Nwitht
print(decayFunc(10,0.005)) #test
[a,b,c]=decayFunc(10,0.005) #test
###problem solving
lambd=0.005
t=[0]*1000 
N=[0]*1000 
N[0]=2
for i in range(1,1000):
    [t[i-1],b[i-1],c[i-1]]=decayFunc(i,lambd)
    N[i]=N[i-1]+1
    N[i-1]=math.log(N[i-1],math.e)
N[999]=math.log(N[999],math.e)
plt.plot(N,t,"bo")
plt.ylabel("time")
plt.xlabel("ln(N)")
##problem 3
plt.plot(b[50])
plt.plot(b[997])
##problem 4 
plt.plot(c[221])
plt.plot(c[997])
##problem 5
plt.plot(c[997],b[997])


