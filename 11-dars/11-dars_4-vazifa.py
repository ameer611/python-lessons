# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:42:27 2023

@Ameer
"""

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat 
# yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, 
# mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi 
# so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa 
# mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar
# do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni 
# chiqaring.




mahsulotlar = ['guruch', 'karto\'shka', 'piyoz', 'sabzi', 'loviya', 'go\'sht', 'mosh', 'yasmiq', 'ko\'cha', 'yog\'']
savat = []
bor_mahsulotlar = []
mavjud_emas = []



for son in range(5):
    savat.append(input(f"{son+1}-o'zingizga kerakli mahsulotni savatga qo'shing: "))


print('\n')


if savat:
    for maxsulot in savat:
        if maxsulot.lower() in mahsulotlar:
            bor_mahsulotlar.append(maxsulot)
        else:
            mavjud_emas.append(maxsulot)
else:
    print("Savatchangiz bo'sh!")
    
if len(mavjud_emas) == 0:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
else:
    print('Quyidagi mahsulotlar do\'konimizda yo\'q: ')
    for maxsulot in mavjud_emas:
        print(maxsulot)
    

