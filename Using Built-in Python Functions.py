f1 = "Myfile.txt"
lines =words = chars = spaces = 0

with open(f1, "r") as f:
    for x in f:
        lines += 1
        words += len(x.split())
        spaces += x.count(" ")
        chars += sum(1 for c in x if c not in (" ", "\n"))

print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)
print("Spaces:", spaces)