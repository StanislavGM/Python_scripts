# For loop with an if else condition.
my_list = [3,4,34,5,67,89,23]
for each in my_list:
    rem = each%2
    if rem == 0:
        print(f'{each} is even')
    else:
        print(f'{each} is odd')