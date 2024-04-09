import os
import pandas as pd

current_directory = os.getcwd()

# Construct the file path relative to the current working directory

file_name = 'LaptopsTracker.xlsx'
file_path = os.path.join(current_directory, file_name)
file_path = r'C:\Python\Excel Laptops\LaptopsTracker.xlsx'

df = pd.read_excel(file_path)

pending_rows = df[df.iloc[:, 9].str.lower() == 'pending']

pending_values = pending_rows.iloc[:, 2]

print("Users who didn't return their devices:")
print(pending_values)

