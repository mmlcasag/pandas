import pandas

# ============================================================================== #
# based on the tutorial available at https://www.youtube.com/watch?v=vmEHCJofslg #
# ============================================================================== #

dataframe = pandas.read_csv('./input/data.csv')

# adding a column
dataframe['Total'] = dataframe['HP']      + \
                     dataframe['Attack']  + \
                     dataframe['Defense'] + \
                     dataframe['Sp. Atk'] + \
                     dataframe['Sp. Def'] + \
                     dataframe['Speed']

# displaying the new column
print(dataframe.sort_values(['Total'], ascending=False)[0:10])

# deleting a column
dataframe = dataframe.drop(columns=['Total'])

# diplaying the dataframe with the column removed
print(dataframe)

# another way of adding a column
# : means all rows
# 4:9 means from column index 4 through column index 9 (always the column you want to plus 1)
# axis=1 sums horizontally whereas axis=0 sums vertically
dataframe['Total'] = dataframe.iloc[:, 4:10].sum(axis=1)

# displaying the new column
print(dataframe.sort_values(['Total'], ascending=False)[0:10])

# rearranging columns
dataframe = dataframe[['#', 'Name', 'Type 1', 'Type 2', 'Legendary', 'Generation', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total']]

print(dataframe.head(5))

# another way to rearrange columns
# this will return all the columns into one array
cols = list(dataframe.columns.values)
# cols[0:4] will return '#', 'Name', 'Type 1', 'Type 2'
# [cols[-1]] will return 'Total' --> i had to surround it with square brackets because otherwise it returns a string e throws an error because it is only a single element
# cols[4:12] will return 'Legendary', 'Generation', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'
dataframe = dataframe[cols[0:4] + [cols[-1]] + cols[4:12]]

print(dataframe.head(5))

