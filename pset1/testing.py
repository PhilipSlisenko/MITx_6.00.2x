# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:43:42 2019

@author: slise
"""

#try:
#    l = ["a", "b"]
#    int(l[2])
#except ValueError or IndexError as e:  # To catch both exceptions, right?
#    print(e)

#l = ['a', 'b', 'c', 'd']
#for i in l:
#    print(i)
#    l = l[:-1]
#print(l)
odd = lambda x : bool(x % 2)
numbers = [n for n in range(10)]
print(id(numbers))
numbers += [n for n in numbers if not odd(n)]  # ahh, the beauty of it all
print(id(numbers))
print(numbers)