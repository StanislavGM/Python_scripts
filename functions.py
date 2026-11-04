# Intro.
'''
import os
import time
import platform

if platform.system() == "Windows":
    print("Please wait. It's cleaning the screen...")
    time.sleep(2)
    os.system('cls')
    print("Please wait while it's finding the list of dir and files...")
    time.sleep(2)
    os.system('dir')
else:
    print("Please wait. It's cleaning the screen...")
    time.sleep(2)
    os.system("clear")
    print("Please wait while it's finding the dir and files...")
    time.sleep(2)
    os.system("ls -ltr")
'''
import os
import time
import platform

def mycode(cmd1,cmd2):
    print("Please wait. It's cleaning the screen...")
    time.sleep(2)
    os.system(cmd1)
    print("Please wait while it's finding the list of dir and files...")
    time.sleep(2)
    os.system(cmd2)
if platform.system() == "Windows":
    mycode('cls','dir')
else:
    mycode('clear','ls -ltr')
mycode()