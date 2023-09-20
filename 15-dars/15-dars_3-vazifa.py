# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:47:09 2023

@ameer611
"""

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. 
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.


davlatPoytaxtlari = {
    'uzbekistan' : 'tashkent',
    'russia' : 'moskow',
    'kazakistan' : 'nur sultan',
    'kirgizistan' : 'bishkek',
    'italia' : 'roem',
    'france' : 'paris',
    'tajikistan' : 'dushanbe',
    'afganistan' : 'kabul',
    'turkmenistan' : 'ashgabat'
    }

country = input('Istalgan davlatingizni kiriting: ').lower()    
poytaxt = davlatPoytaxtlari.get(country)

if poytaxt == None:
    print("Bizda bunday ma'lumot yo'q")
else:
    print(f"{country.upper()}ning poytaxti {poytaxt.title()}")