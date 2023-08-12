# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:40:55 2023

@Ameer
"""

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# Ro'yxatdagi elementlar sonini hisoblang
# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring


juftSonlar = list(range(120, 1201, 2))


sumJuftSonlar = sum(juftSonlar)


elemenlarSoni = len(juftSonlar)


print(sumJuftSonlar, '\n')


print(max(juftSonlar)-min(juftSonlar), '\n')


print(elemenlarSoni, '\n')


print(juftSonlar[:20], '\n')


print(juftSonlar[-20:], '\n')


print(juftSonlar[260:280], '\n')