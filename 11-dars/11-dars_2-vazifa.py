# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:25:58 2023

@Ameer 
"""

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm


yosh = int(input('Yoshingizni kiriting: '))
narx = 0

if yosh<4 or yosh>60:
    narx=0
elif yosh<=18:
    narx=10_000
elif yosh>18:
    narx=20_000
    

if narx == 0:
    print('Siz uchun Muzeyga kirish bepul.')
else:
    print('Siz uchun Muzeyga kirish', narx, "so'm.")
