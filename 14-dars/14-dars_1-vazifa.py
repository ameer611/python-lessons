# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 09:44:54 2023

@ameer611

14-dars
"""

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson 
# haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). 
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: 
# Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan


herFather = {
    'name' : 'Melis',
    'bornYear' : 1985,
    'bornWhere' : "Termiz"
    }

herMother = {
    'name' : 'angelia',
    'bornYear' : 1980,
    'bornWhere' : "Texas"
    }

herBrother = {
    'name' : 'jone',
    'bornYear' : 2005,
    'bornWhere' : "toshkent"
    }


print(f'Uning otasining ismi {herFather["name"].title()}, {herFather["bornYear"]}-yilda, {herFather["bornWhere"].title()}da tug\'ulgan.')

print(f'Uning onasining ismi {herMother["name"].title()}, {herMother["bornYear"]}-yilda, {herMother["bornWhere"].title()}da tug\'ulgan.')

print(f'Uning akasining ismi {herBrother["name"].title()}, {herBrother["bornYear"]}-yilda, {herBrother["bornWhere"].title()}da tug\'ulgan.')


