# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:27:14 2023

@Ameer
"""

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# Ro'yxatning uzunligini konsolga chiqaring
# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# Asl ro'yxatni qaytadan konsolga chiqaring
# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.



davlatlar = ['Germaniya', 'O\'zbekiston', 'Rossiya', 'Italiya', 'Shvetsiya', 'Braziliya']

print(len(davlatlar), '\n')


print(sorted(davlatlar), '\n')


print(sorted(davlatlar, reverse=True), '\n')


print(davlatlar, '\n')


davlatlar.reverse()
print(davlatlar, '\n')


davlatlar.sort()
print(davlatlar, '\n')


davlatlar.sort(reverse=True)
print(davlatlar, '\n')


