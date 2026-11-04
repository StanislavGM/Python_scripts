# Script to make an addition.
a = 4
b = 8
result = a + b
#print('The addition of {} and {} is {}'.format(a,b,result))
print(('The addition of {} and {} is {}').format(a,b,result))


num = eval(input("Please enter younr number from a range 1-10: "))
num_word = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}
if num in num_word:
    print(num_word.get(num))
else:
    print("The number you entered is not in the range")