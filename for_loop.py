# Intro
import os
import sys
path = input("Please enter your path: ")
if os.path.exists(path):
    df_l = os.listdir(path)
else:
    print("THe path your entered is wrong, please enter a valid path")
    sys.exit()
for each in df_l:
    f_d_p = os.path.join(path, each)
    if os.path.isfile(f_d_p):
        print(f'{f_d_p} is a file')
    else:
        print(f'{f_d_p} is a directory')