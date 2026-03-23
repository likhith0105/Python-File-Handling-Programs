import pandas as pd

df = pd.read_csv("myfile.txt", header=None)
df.drop_duplicates(inplace=True)
df.to_csv("output.txt", index=False, header=False)