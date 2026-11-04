# Script to write the content of the variable to the file or to stdout. Read the content from the given file.
import os
import sys
'''
fo = open('new_file.txt', 'w')
print(fo.mode)
print(fo.readable())
print(fo.writable())
'''
'''
fo = open('new_file.txt', 'w')
fo.write('This is a first line\n')
fo.write('This is a second line\n')
fo.write('This is a third line')
fo.close()
'''
'''
my_cont = ['This is a data-1\n', 'This is a data-2\n', 'This is a data-3']
fo = open('random.txt', 'w')
fo.writelines(my_cont)
fo.close()
'''
'''
my_cont = ['This is using loop-iteration-1', 'This is using loop-iteration-2', 'This is using loop-iteration-3']
fo = open('with_loop.txt', 'w')
for each_line in my_cont:
    fo.write(each_line+"\n")
fo.close
'''
'''
my_cont = ['This is using loop-iteration-1', 'This is using loop-iteration-2', 'This is using loop-iteration-3']
fo = open('with_loop.txt', 'r')
print(fo.readline())
print(fo.readline())
fo.close
'''
my_cont = ['This is using loop-iteration-1', 'This is using loop-iteration-2', 'This is using loop-iteration-3']
fo = open('with_loop.txt', 'r')
data = fo.readlines()
fo.close
#for each_line in range(3):
#    print(data[each_line])
print(data[-1])