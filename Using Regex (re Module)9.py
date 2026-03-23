import re

f1 = open('myfile1.txt', 'r')
f2 = open('myfile2.txt', 'w')

for line in f1:
    if not re.match("^TextGenerator", line):  
        print(line, end=' ')
        f2.write(line)

f1.close()
f2.close()