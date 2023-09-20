# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:35:04 2023

@ameer611
"""

# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring

davlatPoytaxtlari = {
    'uzbekistan' : 'tashkent',
    'russia' : 'moskow',
    'kazakistan' : 'nur sultan',
    'kirgizistan' : 'bishkek',
    'italia' : 'roem',
    'farance' : 'paris'
    }

print('Davlatlar: ')

for davlat in sorted(davlatPoytaxtlari.keys()):
    print(davlat.title())

print('\n\nPoytaxtlar: ')

for poytaxt in sorted(davlatPoytaxtlari.values()):
    print(poytaxt.title())
