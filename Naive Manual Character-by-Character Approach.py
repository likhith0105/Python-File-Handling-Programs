with open("Myfile.txt", "r") as f:
    w = ""
    for ch in f.read():   
        if ch == " " or ch == "\n":
            if w:
                print(w)
                w = ""         
        else:
            w += ch            
    if w:
        print(w)