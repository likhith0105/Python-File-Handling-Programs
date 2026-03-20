fname = "File1.txt"
words = lines = chars = spaces = 0

with open(fname, "r") as f:
    for line in f:
        lines += 1
        flag = True

        for ch in line:
            if ch != " " and ch != "\n" and flag:
                words += 1
                flag = False
            elif ch == " ":
                spaces += 1
                flag = True

            if ch not in (" ", "\n"):
                chars += 1

print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)
print("Spaces:", spaces)