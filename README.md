# laptoptracker-python

This script is designed to read data from an Excel file using Python's pandas library. It performs operations to filter and analyze the data, and then prints the results.

Steps in the Script:

Importing Libraries:

The script imports the pandas library using the alias pd. This library provides powerful data manipulation and analysis tools for Python.
Constructing File Path:

The script dynamically constructs the file path of the Excel file to be read. It uses the os module to get the current working directory and joins it with the file name to create the file path. This ensures that the script can locate the Excel file relative to its location.
Reading Excel Data:

The pd.read_excel() function is used to read the data from the Excel file located at the constructed file path. The data is loaded into a pandas DataFrame (df), which is a tabular data structure similar to a spreadsheet.
Filtering Data:

The script filters the rows in the DataFrame based on a specific condition. It selects rows where the value in the 10th column (indexing starts from 0) is equal to 'pending'. This is achieved using boolean indexing with pandas.
Extracting Values:

After filtering the data, the script extracts values from specific columns of the filtered rows for further analysis. It selects values from the 3rd column (indexing starts from 0) of the filtered rows.
Printing Results:

The script prints the extracted values, which represent users who haven't returned their devices. It provides a clear message indicating the purpose of the output.
