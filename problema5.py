# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:44:13 2024

@author: ju_je
"""

import math
n = int(input()) # leer un entero N


suma = 0
for i in range(1,int(math.sqrt(n))+1):
    if n%i == 0:
        suma+=i
        if n//i != n:
            suma+=n//i
            
if suma == n:
    print('Es perfecto')
else:
    print('No es perfecto')