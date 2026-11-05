import pandas as pd

data = pd.read_csv("panda/files/homework4.csv")





above75 = data[data[" Maths "]>75]
print(above75.head())