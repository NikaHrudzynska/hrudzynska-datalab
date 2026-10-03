import pandas as pd
import numpy as np

data = {
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


#1-2
df = pd.DataFrame(data, index=labels)
print(df)

#3
print(df.loc['e', 'animal'])

#4
print(df['age'].count())

#5
print(df.iloc[:3])

#6
print(df.iloc[[0, 2, 3]])

#7
print(df[['animal', 'age']])

#8
print(df.iloc[[0, 2, 3]][['animal', 'age']])

#9
print(df[df['age'] > 3])

#10
print(df[df['age'].notna()])

#11
print(df[(df['age'] >= 2) & (df['age'] <= 4)])

#12
df['age'] = df['age'] + 1
print(df)

#13
print(df[df['age'] == df['age'].max()])

#14
print(df['age'].sum())

#15
print(df[df['animal'] == 'cat'])

#16
print(df[(df['animal'] == 'dog') & (df['visits'] > 1)])

#17
print(df[df['priority'] == 'yes'])

#18
print(df[(df['priority'] == 'no') & (df['age'] >= 3)])

#19
print(df[df['visits'] == 1][['animal', 'visits']])

#20
print(df[df['animal'].isin(['cat', 'snake'])])

#21
print(df[(df['age'] < 3) | (df['age'].isna())])

#22
print(df[(df['visits'] >= 2) & (df['visits'] <= 3)])

#23
print(df.loc[['a', 'c', 'f']])

#24
print(df[df['animal'] != 'dog'])
