import pandas as pd
import os

# Set your folder path and output file name
folder_path = r'C:\Users\dylan\OneDrive\Documents\Sample_CSV_Data'
output_file = 'combined.xlsx'

# Create a pandas Excel writer using openpyxl
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            # Read the CSV into a dataframe
            df = pd.read_csv(file_path)
            # Write to a sheet named after the file (without .csv)
            sheet_name = os.path.splitext(filename)[0]
            df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"All CSV files from '{folder_path}' combined into '{output_file}' successfully.")
