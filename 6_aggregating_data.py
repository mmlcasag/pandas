import pandas

# ============================================================================== #
# based on the tutorial available at https://www.youtube.com/watch?v=vmEHCJofslg #
# ============================================================================== #

dataframe = pandas.read_csv('./input/data.csv')

# column averages grouped by Type 1
print(dataframe.groupby(['Type 1']).mean())

# column averages grouped by Type 1 sorted by highest average of Defense
print(dataframe.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))

# column averages grouped by Type 1 sorted by highest average of Attack
print(dataframe.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

# column averages grouped by Type 1 sorted by highest average of HP
print(dataframe.groupby(['Type 1']).mean().sort_values('HP', ascending=False))

# column sums grouped by Type 1
print(dataframe.groupby(['Type 1']).sum())

# column counts grouped by Type 1
print(dataframe.groupby(['Type 1']).count()['#'])

# grouping data by multiple columns
print(dataframe.groupby(['Type 1', 'Type 2']).count()['#'])
