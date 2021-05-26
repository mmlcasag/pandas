import pandas
import re

# ============================================================================== #
# based on the tutorial available at https://www.youtube.com/watch?v=vmEHCJofslg #
# ============================================================================== #

dataframe = pandas.read_csv('./input/data.csv')

# how to filter the dataframe with a single condition
print('Filter #1')
print(dataframe.loc[dataframe['Type 1'] == 'Grass'])

# how to filter the dataframe with multiple conditions (using AND operator)
print('Filter #2')
print(dataframe.loc[ 
    (dataframe['Type 1'] == 'Grass') 
  & 
    (dataframe['Type 2'] == 'Fighting')
])

# how to filter the dataframe with multiple conditions (using OR operator)
print('Filter #3')
print(dataframe.loc[ 
    (dataframe['Type 1'] == 'Grass') 
  | 
    (dataframe['Type 2'] == 'Fighting')
])

# how to filter the dataframe with multiple conditions (using AND operator)
print('Filter #4')
print(dataframe.loc[ 
    (dataframe['Type 1'] == 'Grass') 
  & 
    (dataframe['Type 2'] == 'Poison')
  &
    (dataframe['HP'] > 70)
])

# how to filter the dataframe with just a piece of a string, just like SQL's LIKE operator
print('Filter #5')
print(dataframe.loc[
    dataframe['Name'].str.contains('Mega')
])

# how to filter the dataframe using the NOT operador
print('Filter #6')
print(dataframe.loc[
    ~dataframe['Name'].str.contains('Mega')
])

# whenever you filter you dataframe, it returns as the first row the id of the previous dataframe
# if this is annoying to you, you can reset the index
new_dataframe = dataframe.loc[ 
    (dataframe['Type 1'] == 'Grass') 
  & 
    (dataframe['Type 2'] == 'Poison')
  &
    (dataframe['HP'] > 70)
]

# by default reset_index keeps as a new column the previus index
# you can remove that by passing the argument drop=True
new_dataframe.reset_index(inplace=True, drop=True)

print('Reset Index:')
print(new_dataframe)

# regex filtering
print('Regex #1')
print(dataframe.loc[
    dataframe['Type 1'].str.contains('Fire|Grass', regex=True)
])

# regex filtering ignoring case
print('Regex #2')
print(dataframe.loc[
    dataframe['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)
])

# regex filtering names that start with pi
print('Regex #3')
print(dataframe.loc[
    dataframe['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)
])
