# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:06:59 2023

@Ameer
"""

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi 
# login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning 
# tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.


loginlar = ['anvar', 'aziz', 'hakim', 'olim', 'hasan']
yangiLogin = input("Yangi login tanlang: ")


if yangiLogin:
    if yangiLogin.lower() in loginlar:
        print("Login band, yangi login tanlang!")
    else:
        print("Xush kelibsiz,", yangiLogin.title()+"!")
else:
    print("Siz hech qanday login kiritmadingiz!")