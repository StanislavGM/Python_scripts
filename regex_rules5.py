# Regex to search pattern which includes python, python2, python3.
import re
text = "This is for python and there are two major vers python2 and python3 in future python4"
'''
pat = r'\bpython\b'
print(re.findall(pat,text))
'''
'''
pat = r'\bpython[23]\b'
print(re.findall(pat,text))
'''
'''
pat = r'\bpython\d?\b' -- в условии может присутствовать 1 цифра.
print(re.findall(pat,text))
'''
'''
pat = r'\bpython\d?\b'
match_ob = re.search(pat,text)
print(match_ob)
'''
'''
pat = r'\bpython\d?\b'
match_ob = re.search(pat,text)
if match_ob:
    print("Match from your pattern: ", match_ob)
    print("Starting index: ", match_ob.start())
    print("Ending index: ", match_ob.end())
    print("length ", match_ob.end() - match_ob.start())
else:
    print("No match found")
'''
text2 = """PYTHON2 and there are two major 
vers python2 and python3 in future python4"""
pat = r'\bpython[2,3]?\b'
match_ob = re.match(pat, text2, re.I)
if match_ob:
    print("Match from your pattern: ", match_ob)
    print("Starting index: ", match_ob.start())
    print("Ending index: ", match_ob.end())
    print("length ", match_ob.end() - match_ob.start())
else:
    print("No match found")