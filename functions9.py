# Function displays the keyword arguments of variables.
'''
def display(a, **kwags):
    print(a, kwags)
    return None
#display(x = 5, y = "Hi", z = 6.7, user = "root")
display(4, x = 5, y = "Hi", z = 6.7, user = "root")
'''
'''
def display(*data):
    print(data)
    return None
display(4,5,67,"root")
'''
def display(*args):
    for each in args:
        print(type(args)) # Тип данных будет в виде <class 'tuple'>
    return None
display("hi", 4.65)