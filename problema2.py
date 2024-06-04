# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:44:12 2024

@author: ju_je
"""

n = int(input())

new_number = n * 10

suma = 0
for i in range(3):
    digit = n%10
    n//=10
    
    if i == 0:
        suma+=(digit*5)
    if i == 1:
        suma+=(digit*3)
    if i == 2:
        suma+=digit
    

suma%=7
new_number+=suma

print(new_number)