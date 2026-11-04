# Intro
my_list = [0, 4, 6]
try:
    print(f'{my_list[0]}{my_list[1]}{my_list[3]}')
except Exception as Exception:
    print("Here is exception: ", Exception)
print("This string will also be printed aside of generic function")