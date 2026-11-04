# For loop to print the pieces of entered string.
my_str = input("Please enter your string: ")
''' 1-й способ
for str in range(len(my_str)):
    id = range(len(my_str))
    print(f'{str} --> {my_str[str]}')
''' 
''' 2-й способ
usr_str = input("Please enter your string")
for str in range(len(my_str)):
    print(f'{str} --> {my_str[str]}')
    index = index +1
'''
'''не правильный вариант'''
for str in my_str:
    print(f'{str} --> {len(int(my_str[str]))}')