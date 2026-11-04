# Script to do copy content of the file to the new one.
sfile = input("Please input an absolute path of your file: ")
dfile = input("Please input an absolute path of your destination file: ")
sfo = open(sfile)
content = sfo.read()
sfo.close

dfo = open(dfile, 'w')
dfo.write(content)
dfo.close()