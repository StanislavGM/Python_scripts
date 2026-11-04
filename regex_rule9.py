# Regex to make substitution of the founded matches.
import re
my_str = "This is about python and python is very easy and we are having python2 vers and Python3 vers"
my_pat = r'\bpython[23]?\b'
'''
print(re.split(my_pat,my_str,maxsplit=2,flags=re.I)) - вывод определенного кол-ва совпадений
'''
'''
print(re.sub(my_pat,'jython',my_str,flags=re.I)) - замена найденных совпадений на указываемую строку
'''
'''
print(re.sub(my_pat,'jython',my_str,count=2,flags=re.I)) -  замена найденных совпадений с указанием кол-ва на указываемую строку
'''
print(re.subn(my_pat,'jython',my_str,count=4,flags=re.I)) #- замена найденных совпадений с указанием кол-ва на указываемую строку, также будет вывод кол-ва замененных совпадений.