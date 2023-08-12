# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 09:27:11 2023

@Ameer
"""

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik)
# ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning 
# qiymatini o'zgartiring, ba'zilarini esa almashtiring.

sonlar = [15000, -20, 3.14, 2.7, 11235813, -36.6]


sonlar[0] = sonlar[0] + 5000
sonlar[-1] = 36.6
sonlar[4]= 16.18
del sonlar[1]
sonlar.insert(1, 99)


print (sonlar[0], '+', sonlar[4], '=', sonlar[0]+sonlar[4])
print (sonlar[1], '-', sonlar[5], '=', sonlar[1]-sonlar[5])
print (sonlar[2], '*', sonlar[3], '=', sonlar[2]*sonlar[3])
print (sonlar[0], '/', sonlar[3], '=', sonlar[0]/sonlar[3], '\n')

print(sonlar)

