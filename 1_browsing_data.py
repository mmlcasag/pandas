import pandas

# ============================================================================== #
# based on the tutorial available at https://www.youtube.com/watch?v=vmEHCJofslg #
# ============================================================================== #

# how to read a file
# if you don't specify the number of rows in the parameter, it defaults to ','
dataframe = pandas.read_csv('./input/data.csv', delimiter=',')

# how to print the entire file
print(dataframe)

# how to print just the top of the file
# if you don't specify the number of rows in the parameter, it defaults to 5
print(dataframe.head(5))

# how to print just the bottom of the file
# if you don't specify the number of rows in the parameter, it defaults to 5
print(dataframe.tail(5))

# how to print the file header
print(dataframe.columns)

# how to print a specific header
print(dataframe.columns[3])

# how to print a range of headers
print(dataframe.columns[0:3])

# how to print a specific column
print(dataframe['Name'])
print(dataframe.Name) # this notation does not support multi word columns

# how to print a specific column, but just some rows
print(dataframe['Name'][0:5])
print(dataframe.Name[0:5]) # this notation does not support multi word columns

# how to print specific columns
print(dataframe[['Name', 'Type 1', 'Type 2']][50:60])

# how to print a specific row
print(dataframe.iloc[2])

# how to print multiple rows
print(dataframe.iloc[0:5])

# how to print a cell (intersection of column and a row)
print(dataframe.iloc[4, 2])

# how to iterate through each row
for index, row in dataframe.iterrows():
    print(index, row)

# how to iterate through each row specifying the columns you want to display
for index, row in dataframe.iterrows():
    print(index, row[['Name', 'Type 1', 'Type 2']])

# how to locate (and print) only the rows in which Type 1 is equals to 'Fire'
# this is similiar to SQL's WHERE clause
print(dataframe.loc[dataframe['Type 1'] == 'Fire'])

# how to obtain a high level description of your data
print(dataframe.describe())

# how to sort values by descending list of name 
print(dataframe.sort_values('Name', ascending=False))

# how to sort values by multiple columns
print(dataframe.sort_values(['Type 1', 'Type 2'], ascending=True))
print(dataframe.sort_values(['Type 1', 'Type 2'], ascending=[True, False]))
print(dataframe.sort_values(['Type 1', 'Type 2'], ascending=[0, 1]))
