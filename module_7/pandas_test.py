import pandas as pd

df = pd.read_csv('module_7\\telco_churn.csv')

tempdict = {'Name': ['A', 'B', 'C'], 'Age': [10, 20, 30]}
dictdf = pd.DataFrame.from_dict(tempdict)



print(df.head())

print(df.tail(15))

# 2.2 
print(df.columns)
print(df.dtypes)

# 2.3
print(df.describe())
print(df.describe(include='object'))

# 2.4
print(df.State)
print(df['International plan'])
print(df[['State', 'International plan']])
print(df.State.unique())
# 2.5
print(df.head())
# print(df[df['International plan'] == 'No'])
# print((df[df['International plan'] == 'No']) & df['Churn'] == False)

# 2.6
print(df.iloc[14])
print(df.iloc[14, -1])
print(df.iloc[22:33])

#2.7
state = df.copy()
state.set_index('State', inplace=True)
print(state.head())
print(state.loc['OH'])

#3.1
print(df.isnull().sum())
df.dropna(inplace=True)
print(df.isnull().sum())

#3.2
df.drop('Area code', axis=1, inplace=True)
print(df.head())

#3.3
df['New Column'] = df['Total night minutes'] + df['Total intl minutes']
print(df.head())

#3.4
df['New Column'] = 10
print(df.head())

#3.5
df.iloc[0, -1] = 200
print(df.head())

#3.6
df['Churn Binary'] = df['Churn'].apply(lambda x: 1 if x == True else 0)
print(df.head())

#4.1
df.to_csv('module_7\\telco_churn_new.csv', index=False)

#4.2
df.to_json('module_7\\telco_churn_new.json')

#4.3
df.to_html('module_7\\telco_churn_new.html')

#4.4
del df


