seen = []

with open("myfile.txt", "r") as f_in, open("output.txt", "w") as f_out:
    for ln in f_in:
        if ln not in seen:
            f_out.write(ln)
            seen.append(ln)