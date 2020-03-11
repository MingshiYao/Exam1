# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:49:27 2020

@author: Hasee
"""

import math
import matplotlib.pyplot as plt
def expo(x,n):
    term = 1.0 
    sum = 1.0

    for i in range(1,n-1):
      term = term*x/i
      sum = sum + term 

    return sum

x = float(input("Enter the x: "))
##n= int(input("How many steps you want take:"))

#print("My exponential function exp(x)=",expo(x,n))
print("exp(x) = ", math.exp(x))

fracError=[0]*1000 # Array with 1000 elements 
Diffi=[0]*1000 # Array with 1000 elements 
Diffi[0]=1
for i in range(1,50):
    fracError[i-1]=abs((expo(x,i)-math.exp(x)))/math.exp(x)
    Diffi[i]=Diffi[i-1]+1
plt.plot(Diffi,fracError,"bo")
plt.ylabel("Fractional Error")
plt.xlabel("N")



