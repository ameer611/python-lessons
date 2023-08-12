# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 17:54:54 2023

@Ameer
"""

kocha = input("Ko'changiz nomini kiriting: \n>>>" )     #"Bog'bon"
mahalla = input("Mahallangizni nomini kiriting: \n>>>")  #"Sog'bon"
tuman = input("Tumaningiz nomini kiriting: \n>>>")    #"Bodomzor"
viloyat = input("Viloyatingiz nomini kiriting: \n>>>")  #"Samarqand"

#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

natija = f"{kocha.title()} ko'chasi, \n{mahalla.title()} mahallasi, \n{tuman.title()} tumani, \n{viloyat.title()} viloyati."

print (natija.lower())
print (natija.upper())
print (natija.capitalize())