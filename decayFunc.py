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
    while N > 0:
        DeltaN = 0
        for i in range(N):
            if (random.random() < lambd):
                DeltaN = DeltaN + 1
        t = t + 1
        N = N - DeltaN
    return t

lambd=0.005
t=[0]*10000 # Array with 1000 elements 
N=[0]*10000 # Array with 1000 elements 
N[0]=1
for i in range(1,10000):
    t[i-1]=decayFunc(i,lambd)
    N[i]=N[i-1]+1
    N[i-1]=math.log(N[i-1],math.e)
N[9999]=math.log(N[9999],math.e)
plt.plot(N,t,"bo")
plt.ylabel("time")
plt.xlabel("ln(N)")

