# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:27:50 2023

@Ameer 
"""

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha 
# bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.


son = int(input("Butun son kiriting: "))

for n in range(2, 11):
    if son%n == 0:
        print('Siz kiritgan son', n, 'soniga qoldiqsiz bo\'linadi.')
        
        
