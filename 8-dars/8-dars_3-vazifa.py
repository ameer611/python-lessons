# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:57:10 2023

@Ameer
"""

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# nonushta degan yangi ro'yxatga taomlardan nusxa oling
# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring


taomlar = ['Somsa', 'Osh', 'Lag\'mon', 'Sho\'rva', 'Mastava']


nonushta = taomlar[:]


nonushta.remove('Osh')
nonushta.remove('Somsa')
nonushta.append('Sut')
nonushta.append('Qaymoq')


print(taomlar)
print(nonushta)


nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"



