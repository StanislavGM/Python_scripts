# Regex pattern to check text in multiline mode.
import re
#text = "this is a string This is a new starting THIS"
'''
my_pat = r'this'
print(re.findall(my_pat,text,re.I))
'''
'''
text = """this is a string
this is second line
This is third line
asfasd this"""
my_pat = r'^this'
print(re.findall(my_pat,text,re.M))
'''
'''
text = """this is a string
this is second line
This is third line
asfasd this"""
my_pat = r'^this'
print(re.findall(my_pat,text,re.M|re.I))
'''
text = """this is a string end
this is second line enD
This is third line EnD
asfasd this end"""
my_pat = r'end$'
print(re.findall(my_pat,text,re.M))