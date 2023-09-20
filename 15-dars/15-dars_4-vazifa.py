# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:10:35 2023

@author: user
"""

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
# agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {
        'osh' : 20000,
        'sho\'rva' : 18000,
        "mastava" : 19000,
        'monti' : 5000,
        'somsa' : 10000,
        "dimlama" : 15000,
        "do'lma" : 17000,
        "grill" : 25000,
        "pitsa" : 22000,
        "lavash" : 23000
        }

print('3 ta taom buyurtma bering.')

buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f'{n+1}-taom:  ').lower())

for a in range(3):
    taom = buyurtmalar[a]
    tekshiruv = menu.get(taom)
    
    if tekshiruv == None:
        print("Bizda", taom, "yo'q.")
    else:
        print(taom.title(),'', tekshiruv, 'so\'m')