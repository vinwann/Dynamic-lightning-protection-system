import pandas as pd
import glob

# Assuming your CSV files are in the same directory and have a similar structure
# You may need to adjust the path and file extension based on your actual files

# Path to the directory containing CSV files
csv_files_path = r'C:/Users/vinur/Desktop/arrival/'

# Pattern for file names (assuming all CSV files in the directory should be combined)
file_pattern = '*.csv'

# Get a list of all CSV files in the directory
csv_files = glob.glob(csv_files_path + file_pattern)

# Initialize an empty list to store DataFrames
dfs = []

# Iterate through each CSV file and append its contents to the list
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)

# Combine all DataFrames into one
combined_df = pd.concat(dfs, ignore_index=True)

# Add an index column
combined_df.insert(0, 'Index', range(1, len(combined_df) + 1))


# Save the combined DataFrame to a new CSV file
combined_df.to_csv(r'C:/Users/vinur/Desktop/arrival/arrival_data.csv', index=False)
