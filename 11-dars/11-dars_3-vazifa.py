# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:36:01 2023

@Ameer 
"""

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring


son1 = int(input('1-son kiriting: '))
son2 = int(input('2-son kiriting: '))


if son1 == son2:
    print('Sonlar o\'zaro teng.')
elif son1>son2:
    print(f"{son1} soni, {son2} sonidan katta")
else:
    print(f"{son1} soni, {son2} sonidan kichkina")    
