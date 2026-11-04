# Regex checks for is or it words.
import re
'''
my_str = "Python is simple and it is easy to learn"
print(my_str.split("is"))
print(my_str.split("it"))
'''
my_str = "Python is simple and it is easy to learn"
print(re.split("i[st]", my_str))