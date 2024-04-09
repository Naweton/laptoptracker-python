import os
import pandas as pd

# Get the current working directory
current_directory = os.getcwd()

# Construct the file path relative to the current working directory
file_name = 'LaptopsTracker.xlsx'
file_path = os.path.join(current_directory, file_name)

# Read data from the Excel file
df = pd.read_excel(file_path)

# Filter rows where the value in the 10th column is 'pending'
pending_rows = df[df.iloc[:, 9].str.lower() == 'pending']

# Extract values from the 3rd column of the filtered rows
pending_values = pending_rows.iloc[:, 2]

# Print the extracted values
print("Users who didn't return their devices:")
print(pending_values)

