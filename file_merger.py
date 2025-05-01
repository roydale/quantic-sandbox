import pandas as pd
import os

def list_columns(df, file_label):
    print(f"\nColumns in {file_label}:")
    for i, col in enumerate(df.columns):
        print(f"{i}: {col}")
    return df.columns

def get_column_selection(columns, file_label):
    while True:
        try:
            index = int(input(f"Select the column number from {file_label} to merge on: "))
            if 0 <= index < len(columns):
                return columns[index]
            else:
                print("Invalid column number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    # Step 1: Ask for file names
    current_directory = os.getcwd()
    folder_directory = f"{current_directory}\\merger_files"
    output_file_path = f"{folder_directory}\\merged_output.xlsx"
    
    file1 = input("Enter the name of the first Excel file (e.g., file1.xlsx): ").strip()
    file2 = input("Enter the name of the second Excel file (e.g., file2.xlsx): ").strip()

    # Step 2: Read files and list columns
    df1 = pd.read_excel(f"{folder_directory}\\{file1}")
    df2 = pd.read_excel(f"{folder_directory}\\{file2}")

    cols1 = list_columns(df1, "File 1")
    cols2 = list_columns(df2, "File 2")

    # Step 3: Get user-selected merge columns
    merge_col1 = get_column_selection(cols1, "File 1")
    merge_col2 = get_column_selection(cols2, "File 2")

    # Step 4: Merge and save output
    merged = pd.merge(df1, df2, left_on=merge_col1, right_on=merge_col2)
    merged.to_excel(output_file_path, index=False)
    print(f"\nMerge complete! Output saved to {output_file_path}")

if __name__ == "__main__":
    main()
