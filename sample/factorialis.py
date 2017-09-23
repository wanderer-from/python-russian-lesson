#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 18:33:48 2017

@author: michael
"""

print ("\n\nРасчет факториала циклом WHILE")
n = 10
fac = 1
i = 0
while i<n:
    fac = fac + fac * i
    i = i + 1
    print(i, fac)


print ("\n\nРасчет факториала циклом FOR")
n = 10
fac = 1
for i in range (0, n):
    fac = fac + fac * i
    print(i+1, fac)
    
print ("\n\n Балуемся со строками в FOR")
for i in 'hello world':
    print(i * 2, end='')
    
print ("\n\n Балуемся со строками в FOR и CONTINUE")
for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')
    
print ("\n\n Балуемся со строками в FOR и BREAK")
for i in 'hello world':
    if i == 'o':
        break
    print(i * 2, end='')
    
print ("\n\n Балуемся со строками в FOR и ELSE")
for i in 'hello world':
    if i == 'o':
        print ('Буква \'o\' в строке есть')
        break
else:
    print('Буквы \'o\' в строке нет')
