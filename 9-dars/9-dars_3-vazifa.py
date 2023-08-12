# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:34:33 2023

@Ameer
"""

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.



kinolar = []
print('5 ta sevimli kinoyingizni kiriting!!!')
for son in range(5):
    kinolar.append(input(f"{son+1}-sevimli kinoyingizni kiriting: "))
    
print(kinolar)
    