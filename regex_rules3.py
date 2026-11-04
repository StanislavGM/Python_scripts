# Regex pattern matches last character, defined number of times in curly braces. Also * pattern matches character that can exists in plural sight or not before it. Also + pattern matches character that must exist one or more times.
import re
text = 'This is a pythonnnn and python3 python4 aaa haadafd xyzaaaaaaaa'
'''
my_pat = 'python{4}'
print(re.findall(my_pat, text))
'''
'''
my_pat = r'\bpython{4}\b'
print(re.findall(my_pat, text))
'''
'''
my_pat = r'\bxyza{8}\b' -- последний символ условия повторится 8 раз.
print(re.findall(my_pat, text))
'''
text2 = "xz xaz asdfa sdf xaaz xaaaaaaaaaz xaaaaz"
'''
my_pat = r'\bxa{1,4}z\b' - символ может повторится от 1 до 4 раз
print(re.findall(my_pat, text2))
'''
'''
my_pat = r'\bxa{2,}z\b'
print(re.findall(my_pat, text2))
'''
'''
my_pat = r'\bxa+z\b' -- вариант №2 r'\bxa{1,}z\b'
print(re.findall(my_pat, text2))
'''
'''
my_pat = r'\bxa*z\b' -- символ а может не присутствовать или может повторятся неопред. кол-во раз.
print(re.findall(my_pat, text2))
'''
my_pat = r'\bxa?z\b' #-- символ а может не присутствовать или присутствовать однажды.
print(re.findall(my_pat, text2))