#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 00:07:33 2017

@author: michael
"""

import random

# Введение
print ("\n","*"*40) # здесь \n - это перевод строки а "*" умножается на 40
print ("Вас приветствует искусственный интеллект AI-v.0.002. \n Я еще маленький и только учусь. \n ")
name = input ("Как тебя зовут?\n -->   ")
print ("\n","*"*40,"\n")
print ("Рад приветствовать тебя:", name, "!")

#Диалог про игру
print("Хочешь, сыграем в кости!")

ans = input ("да/нет >>> ")
if ans == "да":
    # здесь играем
    dice_bot = random.randint(1, 6) # бросает бот
    dice_user = random.randint(1, 6) # бросает юзер
    
    print("У меня выпало", dice_bot, "|", "У тебя выпало", dice_user, "\n", sep=" ") 
    
    # сравниваем результат
    if dice_bot > dice_user:
        print("Я победил!")
    elif dice_bot < dice_user:
        print("Ты победил!")
    else:
        print("Ничья!")
        
elif ans == "нет":
    # здесь не играем
    print("До новых встреч, ", name, "!\n", sep="")
else :
    # здесь тоже не играем
    print("Я не понял ответ!\nДо новых встреч, ", name, "!", sep="")

# Концовка диалога   
print ("\n","*"*40,  "\nРАБОТА ОСТАНОВЛЕНА! Дальше общаться меня еще не научили :(")