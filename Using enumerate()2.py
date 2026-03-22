word = "writer"

with open("file1.txt", 'r') as f:
    for n, line in enumerate(f, start=1):
        if word in line:
            print("The word", word, "is found in line number:", n)
            break
    else:
        print("The word", word "is not found in the file.")