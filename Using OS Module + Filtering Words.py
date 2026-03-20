import os
f1 = "Myfile.txt"

lines = words = chars = spaces = 0

with open(f1, "r") as f:
    for x in f:
        line = x.strip(os.linesep)
        wl = x.split()

        lines += 1
        words += len(wl)
        chars += sum(1 for c in line if c not in (" ", os.linesep))
        spaces += sum(1 for c in line if c in (" ",))

print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)
print("Spaces:", spaces)