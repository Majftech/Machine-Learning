"""
analyzes a wine quality dataset taken from the UCI Machine Learning Repository here. Each row contains data on a wine sample, including several physicochemical properties gathered from tests, as well as a quality rating evaluated by wine experts.

The code in this notebook first renames the columns of the dataset and then calculates some statistics on how some features may be related to quality ratings. Can you refactor this code to make it more clean and modular?
"""

import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
df.head()

"""
Renaming Columns
You want to replace the spaces in the column labels with underscores to be able to reference columns with dot notation. Here's one way you could've done it.
"""

df.columns = [label.replace(' ', '_') for label in df.columns]
df.head()

"""
Analyzing Features
Now that your columns are ready, you want to see how different features of this dataset relate to the quality rating of the wine. A very simple way you could do this is by observing the mean quality rating for the top and bottom half of each feature. The code below does this for four features. It looks pretty repetitive right now. Can you make this more concise?

You might challenge yourself to figure out how to make this code more efficient! But you don't need to worry too much about efficiency right now - we will cover that more in the next section.
"""

def numeric_to_buckets(df, column_name):
    median = df[column_name].median()
    for i, val in enumerate(df[column_name]):
        if val >= median:
            df.loc[i, column_name] = 'high'
        else:
            df.loc[i, column_name] = 'low' 
            
for feature in df.columns[:-1]:
    numeric_to_buckets(df, feature)
    print(df.groupby(feature).quality.mean(), '\n')
