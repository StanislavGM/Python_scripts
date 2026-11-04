# Difference between exceptions with conditions else, finalyy.
a = 9
try:
    print(a)
except NameError:
    print("The variable 'a' isn't defined")
except Exception as var:
    print("Exception occured", var)
else:
    print("This will be executed if there are no exception in try block")
finally:
    print('This will be executed always')