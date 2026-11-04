# Regex has a few condition to check [is, it, tablespace, word-pattern at the end or elsewhere].
import re
text = 'it is a python and learn it learnis easy to \n learn'
'''
my_pat = 'i[ts]'
print(re.findall(my_pat, text))
'''
'''
my_pat = '^i[ts]' -- поиск строки только вначале предложения
print(re.findall(my_pat, text))
'''
''' -- поиск строки только вконце предложения
my_pat = 'learn$'
print(re.findall(my_pat, text))
'''
'''
my_pat = r'\blearn' - поиск условия в составе слов
print(re.findall(my_pat, text))
'''
'''
my_pat = r'\blearn\b' - поиск условия расположенного в отдельно от других знаков.
print(re.findall(my_pat, text))
'''
'''
my_pat = r'\Blearn\B' -- поиск условия, которое может располагатся между знаками вначале и в конце. Пр. andlearnit
print(re.findall(my_pat, text))
'''
'''
my_pat = r"\t"
print(re.findall(my_pat, text))
'''
my_pat = r'\n'
print(re.findall(my_pat, text))