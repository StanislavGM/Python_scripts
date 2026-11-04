# Regex with using finditer to print all matches.
import re
my_str = "This is python an we are having python2 and python3 version"
my_pat = r'\bpython[23]?\b'
'''
print(re.match(my_pat, my_str))
'''
'''
print(re.search(my_pat,my_str))
'''
'''
print(re.findall(my_pat,my_str))
'''
'''
print(len(re.findall(my_pat,my_str)))
'''
'''
print(re.finditer(my_pat,my_str))
'''
'''
for each_ob in re.finditer(my_pat,my_str):
    print(each_ob)
'''
for each_ob in re.finditer(my_pat, my_str):
    print("The match is {} starting index: {}, ending index {}".format(each_ob.group(),each_ob.start(),each_ob.end()))