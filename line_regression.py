# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:03:33 2017

@author: yanshan

Liner Regression using only Python built-in element.

Issues to be solved:
    1. When w and b is improper, the result of cost might be too large.
    2. how to set the initial value of 'w' and 'b', to avoid calculation overflow.
    3. how to choose the value of alpha and thresh.
    

"""

#%%

#import numpy as np
import random as rd


#X = np.arange(1, 10, 0.2);

num = 100

X = list(range(num))
Y = []

#Y = 4*X + 5
for i in range(num):
    Y.append(4*X[i]+5)

#w0 = rd.random()
#b0 = rd.random()

alpha = 0.001
epoch = 10000
thresh = 0.001

w = 1
b = 2
for i in range(epoch):
    
    e_w = 0
    e_b = 0
    for j in range(num):
        e_w = e_w + ((w * X[j] + b - Y[j]) * X[j]) / num
        #print("e_w = %f" %e_w)
        e_b = e_b + ((w * X[j] + b - Y[j])) / num
        #print("e_b = %f" %e_b)
    
    w = w - alpha * e_w
    b = b - alpha * e_b


 
    e = 0
    for j in range(num):
       e = e + ((w  * X[j] + b - Y[j])**2)/2
    
    if e < thresh :
        print("Current epoch is %d" %i)
        break

print("w = %f, b = %f" % (w, b))




#%%




