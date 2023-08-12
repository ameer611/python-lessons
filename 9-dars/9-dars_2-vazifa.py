# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:29:48 2023

@Ameer
"""

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.



toqSonlar = list(range(11, 100, 2))
for son in toqSonlar:
    print(son, 'sonining kubi', (son**3), 'ga teng.')
    
    
