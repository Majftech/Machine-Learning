import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
df.head()

df.columns = [label.replace(' ', '_') for label in df.columns]
df.head()

