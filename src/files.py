# "r" for reading files

f = open('10_01_file.txt', 'r')
print(f)

f.readline()

f = open('10_01_file.txt', 'r')
for line in f.readlines():
    print(line.strip())     #strip function removes new line

# "w" for writing to files

f = open('10_01_output.txt', 'w')
print(f)

#   python writes to file via buffer by closing it

f.write('Line 1\n')
f.write('Line 2\n')

f.close()

#   appending to files hence "a"

f = open('10_01_output.txt', 'a')
f.write('Line 3\n')
f.write('Line 4\n')
f.close()


#   best practice to close after writing to a file
#   best way to do this is the "with" statement
#   not only limited to scope
with open('10_01_output.txt', 'a') as f:
    f.write('some stuff\n')
    f.write('some other stuff\n')

print(f)


#   this will return an error because the file is closed

f.write('PS. I forgot some stuff')