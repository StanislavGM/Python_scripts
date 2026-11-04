# Custom exception using assert.
'''
Age = 23
if Age > 30:
    print("The age is valid")
else:
    raise ValueError("The age is less than 30")
'''
'''
assert 4 < 3
'''
Age = 20
try:
    assert Age > 30
    print("The age is valid")
except AssertionError:
    print("Raised with assert because the age is less than 30")