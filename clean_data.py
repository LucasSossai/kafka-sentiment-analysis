import pandas as pd

# Read in the data
df_raw = pd.read_csv('./data/1429_1.csv')

# Get only the columns we want
df_clean = df_raw[["id","reviews.text","reviews.rating"]]

# Rename the columns
df_clean.columns = ["id","text","rating"]

# Shuffle the rows of the dataframe
df_clean = df_clean.sample(frac=1).reset_index(drop=True)

# Export back to csv
df_clean.to_csv('./data/clean_data.csv', index=False)