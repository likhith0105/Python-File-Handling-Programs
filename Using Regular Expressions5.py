import re

fp = "Myfile.txt"
n = 3

with open(fp, 'r') as f:
    text = f.read()

pattern = r'\b\w{' + str(n) + r'}\b'
words = re.findall(pattern, text)

print(f"Words containing {n} characters:")
print(words)