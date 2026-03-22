word = "writer"

with open("file1.txt", 'r') as f:
    res = next((n for n, line in enumerate(f, start=1) if word in line), None)

if res:
    print("The word", word, "is found in line number:", res)
else:
    print("The word", word, "is not found in the file.")