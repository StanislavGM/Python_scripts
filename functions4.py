# Functions with return.
'''
def get_addition(a,b):
    result = a + b
    print("The addition of {} and {} is: {}".format(a,b,result))
    return result
def main():
    a = eval(input("Enter your first number: "))
    b = eval(input("Enter your second number: "))
    result = get_addition(a,b)
    #print("The addition of {} and {} is: {}".format(a,b,result))
    #print(("The addition of {} and {} is: {}").format(a,b,result))
main()
'''
def multiply_num_10(value):
    #result = value * 10 || 1-й способ решения задачи
    #return result
    return value * 10

def main():
    num = eval(input("Enter your number: "))
    var = multiply_num_10(num)
    print("The result is: {}".format(var))
main()