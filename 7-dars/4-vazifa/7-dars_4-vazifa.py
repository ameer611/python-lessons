# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 19:36:07 2023

@Ameer
"""

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida 
# mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.


friends = []


friends.append('amir')
friends.append('akrom')
friends.append('malik')
friends.append('mahmud')
friends.append('anvar')
friends.append('ahmad')


friends.remove('amir')
friends.remove('akrom')


friends.insert(0, 'muso')
friends.insert(2, 'robin')
friends.insert(-1, 'abdulhamid')


mehmonlar = []
mehmonlar = list(mehmonlar)


mehmonlar.append('akrom')
mehmonlar.append('amir')
mehmonlar[0] = friends.pop(0)
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(3))


print (mehmonlar)





