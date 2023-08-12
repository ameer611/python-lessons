# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:54:49 2023

@Ameer 
"""

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. 
# Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring


login = input('Loginingizni kiriting: ')
if login.lower() == 'admin':
    print('Xush kelibsiz, Admin. Foydalanuvchilar ro\'yxatini ko\'rasizmi?')
else:
    print( "Xush kelibsiz,", login.title() + '!')

