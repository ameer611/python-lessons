# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:41:36 2023

@Ameer
"""

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. 
# Ro'yxatni konsolga chiqaring.



insonlarSoni =int(input('Bugun nechta inson bilan suxbatlashdingiz: '))
insonlarIsmi = []
for son in range(insonlarSoni):
    insonlarIsmi.append(input(f"{son+1}-inson isminini kiriting: "))
print('\n', insonlarIsmi)

