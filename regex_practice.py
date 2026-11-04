import re

text = "This is a @python2 and it is easy to learn @X python3"
'''
my_pat = 'is'
print(re.findall(my_pat, text))
print(re.findall('is', 'This is a python and it is easy to learn'))
print(len(re.findall(my_pat, text)))
'''
'''
my_pat = 'i[ts]'
print(re.findall(my_pat, text))
'''
'''
my_pat = '[@asX]'
print(re.findall(my_pat, text))
'''
'''
my_pat = '[a-dh-l-X-z]'
print(re.findall(my_pat, text))
'''
'''
my_pat = '\w\w\w'
print(re.findall(my_pat, text))
'''
'''
my_pat = '\W' '\W Только спец символы '', # $ ! @ и т.д
print(re.findall(my_pat, text))
'''
'''
my_pat = 'python\d'
print(re.findall(my_pat, text))
'''
'''
my_pat = '.' # Все символы, включая - _ @ и т.д.
print(re.findall(my_pat, text))
'''
text2 = "This is my ip_address: 192.168.111.146"
my_pat = '\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d'
print(re.findall(my_pat, text2))