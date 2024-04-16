import pandas as pd

# Load CSV files
stars_df = pd.read_csv('stars_data.csv')
dwarf_stars_df = pd.read_csv('dwarf_stars.csv')

# Convert units in dwarf_stars_df to match units in stars_df
dwarf_stars_df['Distance'] = dwarf_stars_df['Distance'] * 3.262

# Merge data
merged_df = pd.merge(stars_df, dwarf_stars_df, how='outer', on='Name')

# Save merged data to CSV
merged_df.to_csv('merged_data.csv', index=False)
