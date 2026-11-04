# Regex to find all matches with igonre case also.
import re
my_str = "This is about python. Python is easy to learn and we have two major versions: python2 and python3"
'''
my_pat = r'\bpython\b'
print(re.findall(my_pat, my_str))
'''
'''
my_pat = r'\b[pP]ython\b'
print(re.findall(my_pat, my_str))
'''
'''
my_pat = r'\bPython\b'
print(re.findall(my_pat, my_str, flags=re.I))
'''
'''
my_pat = r'\bPython[23]?\b'
print(re.findall(my_pat, my_str, flags=re.I))
'''
'''
my_pat = r'\bPython[23]?\b'
print(re.search(my_pat, my_str))
'''
'''
my_pat = r'\bPython[23]?\b'
print = (re.split(my_pat, my_str, flags=re.IGNORECASE))
'''
'''
my_pat = r'\bPython[23]?\b'
pat_ob = re.compile(my_pat)
print(pat_ob.search(my_str))
'''
my_pat = r'\bPython[23]?\b'
pat_ob = re.compile(my_pat,flags=re.IGNORECASE)
print(pat_ob)
print(pat_ob.findall(my_str))