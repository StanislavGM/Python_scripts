# Example of using shutil to copy file with attributes or without.
import shutil
import time
src = 'shutil_part.py'
dst = "C:\Terraform\Workstation\Terraform\Python\shutil_part.py_bck_up"
#shutil.copyfile(src,dst) - копирование без идентичных разрешений и metadata
#shutil.copy(src,dst) - копирование с идентичными разрешениями, без metadata
#shutil.copy2(src,dst) - копирование с идентичными разрешениями и metadat - ой
#shutil.copymode(src,dst) - копирование только разрешений одного файла в другой
#shutil.copystat(src,dst) - копирование metadata одного файла в другой
'''
src_file = open('continue.py', 'r')
dst_file = open('copied_information.py', 'w')
shutil.copyfileobj(src_file, dst_file)
Функция копирование содержимого из одного файла в другой
'''
src = 'C:\\Terraform\\Workstation\\Terraform\\Python'
dst = 'C:\\Users\\Administrator\\Desktop\\Py_copy'
shutil.copytree(src,dst) # функция рекурсивного копирования каталога с файлами и подкаталогами.
print("Now a new copy of Python dir will be delete")
time.sleep(4)
shutil.rmtree(dst)