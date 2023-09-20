# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:17:33 2023

@ameer611
"""

 # Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
 # Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.


pythonLugatlar = {
    'integer' : 'butun son',
    'float' : 'haqiqiy son',
    'string' : 'matn',
    'if' : 'agar',
    'else' : 'boshqa',
    'print' : 'chop etish',
    'variable' : 'o\'zgaruvchi',
    'list' : "ro'yhat",
    'index' : 'tartib raqami',
    'sort' : "tartiblamoq"
    }

for kalit, qiymat in sorted(pythonLugatlar.items()):
    print(f"{kalit.title()} - '{qiymat}' degan ma'noni bildiradi.")
