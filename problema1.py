# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:44:11 2024

@author: ju_je
"""

import math
n = int(input()) # leer un entero N
es_primo    = 1

if n!=2 and n%2==0:
    es_primo = 0

i = 3
while i <= math.sqrt(n) and es_primo: #O(sqrt(n)/2)
    if n % i == 0:
        es_primo = 0
    i+=2
  

if es_primo:
  print('Es primo')
else:
  print('No es primo')