# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:44:12 2024

@author: ju_je
"""

import math

AB = round(float(input()),2)
BC = round(float(input()),2)
CD = round(float(input()),2)
DA = round(float(input()),2)
AC = round(float(input()),2)

if AB == BC and BC == CD and CD == DA:
    if round(math.sqrt(round(AB**2,2) + round(BC**2,2,)),2) == AC:
        print('Es un cuadrado')
    else:
        print('Es un rombo')
elif AB == CD and DA == BC:
    if round(math.sqrt(round(AB**2,2) + round(BC**2,2,)),2) == AC:
        print('Es un rectangulo')
    else:
        print('Es un paralelogramo')
else:
    print('No existe')