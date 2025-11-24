import pandas as pd

df =  pd.read_csv('titanic.csv')
# print(df.info()) #1

# print(df[df['Sex'] == 'male'].count()) #2.1
# print(df[df['Pclass'] == 1].count()) #2.2

# print(df.groupby('Survived')['Sex'].value_counts()) #3

# print(df.groupby('Pclass')['Fare'].mean()) #4.1
# print(df.groupby('Survived')['Pclass'].value_counts()) #4.2

# print(df['Age'].median()) #5

# df['FamilySize'] = df['Parch']+df['SibSp']+1
# print(df.loc[14,'FamilySize']) #6

# print(df.groupby('Survived')['Age'].mean()) #7

# print(df.groupby(['Survived','Pclass'])['Sex'].value_counts())#8.1
print(df[(df['Age'] < 18) & (df['Parch'] == 0)].count()) #8.2