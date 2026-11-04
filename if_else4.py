# If condition to read the provided path and identify the file directory
import os
import sys
path = input("Enter your directory path: ")
if os.path.exists(path):
    df_l = os.listdir(path)
else:
    print("Please provide a valid path")
    sys.exit()

p1 = os.path.join(path,df_l[0])
p2 = os.path.join(path,df_l[1])

'''
if os.path.isfile(p1):
    print(f'{p1} is a file')
else:
    print(f'{p1} is a directory')

if os.path.isfile(p2):
    print(f'{p2} is a file')
else:
    print(f'{p2} is a directory')
'''
# Способ № 2 если мы не знаем какое кол-во файлов и директорий находится в каталоге.
list_files_or_dirs = os.listdir(path)
print("All files and dirs: ", list_files_or_dirs)
for each_file_or_dir in list_files_or_dirs:
    f_d_p = os.path.join(path, each_file_or_dir)
    if os.path.isfile(f_d_p):
        print(f'{f_d_p} is a file')
    else:
        print(f'{f_d_p} is a directory')
'''
print("Before loop")
for each in [2,3,4]:
    print("ok")
    print("hi")
print("After loop")
'''