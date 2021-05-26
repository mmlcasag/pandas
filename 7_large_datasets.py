import pandas

# ============================================================================== #
# based on the tutorial available at https://www.youtube.com/watch?v=vmEHCJofslg #
# ============================================================================== #

# imagine you are reading a large dataset
# this way you would be loading the entire file all at once (NOT GOOD!)
dataframe = pandas.read_csv('./input/data.csv')

# what you can do instead is this
for dataframe in pandas.read_csv('./input/data.csv', chunksize=50):
    # this reads 50 rows at a time
    print('Chunk')
    print(dataframe)

# another example

# you can create a dataframe from stratch
new_dataframe = pandas.DataFrame(columns=dataframe.columns)

# what you can do instead is this
for dataframe in pandas.read_csv('./input/data.csv', chunksize=50):
    results = dataframe.groupby(['Type 1']).count()
    new_dataframe = pandas.concat([new_dataframe, results])

print(new_dataframe)
