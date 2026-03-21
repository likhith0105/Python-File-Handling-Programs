fp = "Myfile.txt"
n = 3

with open(fp, 'r') as f:
    for line in f:
        for w in line.split():
            if len(w) == n:
                print(w)