# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:44:12 2024

@author: ju_je
"""

n = int(input())

suma = 1

for i in range(n):
    suma = suma * ((i+1)**2)
    
print(suma)