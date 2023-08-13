# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 10:07:41 2023

@ameer611

14-dars
"""

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z 
# (atamani) kiriting (masalan integer, float, string, if, else va hokazo) 
# va har birining qisqacha tarjimasini yozing.

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini 
# yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, 
# "Bunda so'z mavjud emas" degan xabarni chiqaring

# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga 
# tushunarli ko'rinishda chiqaring.


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


suz = input('Qidirayotgan so\'zingizni kiriting: ')
suz = suz.lower()

saerchingWord = pythonLugatlar.get(suz, "Bunday so'z mavjud emas")

if saerchingWord == "Bunday so'z mavjud emas":
    print("Bunday so'z mavjud emas")
else:
    print(f'{suz.title()} so\'zi, "{saerchingWord}" degan ma\'noni anglatadi.')




