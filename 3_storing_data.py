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

# saving modified data to a new file
# you will probably notice that by default, pandas writes the line index as the first column in the spreadsheet
# if you don't want that, you can switch it off by adding the parameter index=False
dataframe.to_csv('./output/generated.csv', index=False)

# you can also export it to txt
dataframe.to_csv('./output/generated.txt', index=False, sep='\t')

# you can also export it to excel in xls format
# in order to do that, you need to add the following dependency
# pip install xlwt 
dataframe.to_excel('./output/generated.xls', index=False)

# you can also export it to excel in xls format
# in order to do that, you need to add the following dependency
# pip install openpyxl 
dataframe.to_excel('./output/generated.xlsx', index=False)

print('Done')
