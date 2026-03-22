word = "writer"

with open("file1.txt", 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    if word in line:
        print("The word", word, "is found in line number:", i)
        break
else:
    print("The word", word, "is not found in the file.")