# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 10:07:11 2023

@Ameer 
"""

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. 
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.


son = int(input('Son kiriting: '))


if son > 0:
    print(son**(1/2))
else:
    print("Musbat son kiriting!!!")

