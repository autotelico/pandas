import pandas as pd

pd.options.display.min_rows=1
pd.options.display.max_rows=5
df = pd.read_csv('source-catalog.csv')
# new_df = df.drop(labels='levelType', axis=1)
new_df = df.sort_values(3, axis=1, ascending=True)

print(new_df)