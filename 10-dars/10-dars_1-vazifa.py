# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:51:12 2023

@Ameer 
"""

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.



cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else: 
        print(car.title())
        
        
    
for car in cars:
    if car != 'gm':
        print(car.title())
    else: 
        print(car.upper())

        
