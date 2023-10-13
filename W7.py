import pandas as pd
pd

#Create from a CSV
df = pd.read_csv('telco_churn.csv')

#Create from a dictionary
tempdict = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}
dictdf = pd.DataFrame.from_dict(tempdict)

#Read
#Show top 5 and bottom 5 rows

df.head(10)

dictdf.head()

df.tail(15)

df.columns

df.dtypes

df.describe()

df.describe(include='object')

df.State
df['International plan']
df[['State', 'International plan']]
df.Churn.unique()

df.head()
df[df['International plan']=='No']
df[(df['International plan']=='No') & (df['Churn']==True)]

df.iloc[14]
df.iloc[14,-1]
df.iloc[22:33]

state = df.copy()
state.set_index('State', inplace=True)
state.head()
state.loc['OH']

df.isnull().sum()
df.dropna(inplace=True)
df.isnull().sum()

df.drop('Area code', axis=1)

df['New Column'] = df['Total night minutes'] + df['Total intl minutes']
df.head()

df['New Column'] = 100
df.head()

df.iloc[0,-1] = 10
df.head()

df['Churn Binary'] = df['Churn'].apply(lambda x: 1 if x==True else 0)
df[df['Churn']==True].head()

df.to_csv('output.csv')

df.to_json()

df.to_html()

del df