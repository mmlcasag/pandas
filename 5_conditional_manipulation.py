import pandas

# ============================================================================== #
# based on the tutorial available at https://www.youtube.com/watch?v=vmEHCJofslg #
# ============================================================================== #

dataframe = pandas.read_csv('./input/data.csv')

# replacing the Type 1 column to 'Flamer' when the Type 1 column is 'Fire'
dataframe.loc[dataframe['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
print(dataframe)

# replacing the Legendary column to 'No Way' when the Type 1 column is 'Grass'
dataframe.loc[dataframe['Type 1'] == 'Grass', 'Legendary'] = 'No Way!'
print(dataframe)

# modifying many columns on a single time
dataframe.loc[dataframe['Speed'] >= 80, ['Generation', 'Legendary']] = 'QUICK_POKEMON'
print(dataframe)

# modifying many columns on a single time
dataframe.loc[dataframe['Speed'] >= 80, ['Generation', 'Legendary']] = ['Quick Generation', 'Quick AND Legendary']
print(dataframe)
