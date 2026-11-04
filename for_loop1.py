# For loop with using break.
my_list = [1,2,3,56,7,8]
for each in my_list:
    print(each)
    if each == 56:
        break #continue
        print('after loop')
print("After loop")