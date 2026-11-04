# For loop to print content of a dictionary or a tuple.
import os
my_dic = {'a':1, 'b':2, 'c':3}
for k,v in my_dic.items():
    print(k,v)
'''
Формат вывода будет:
<class 'str'> <class 'int'>
'''
for each in my_dic.items():
    print(type(each))
'''
формат вывода будет:
<class 'tuple'>
'''