# If else condition to clean the screen.
import platform
import os
os_ver = platform.system()
if os_ver == "Windows":
    os.system('cls')
else:
    os.system('clear')