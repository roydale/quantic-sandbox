import pandas as pd
import os

def read_sales_data(directory_path):
    """
    Reads data from multiple Excel files in a directory.

    Args:
        directory_path (str): The path to the directory containing Excel files.

    Returns:
        dict: A dictionary where keys are file names and values are DataFrames containing the data.
    """
    # Initialize an empty dictionary to store the data from each file
    data_dict = {}

    # List all files in the directory
    file_list = os.listdir(directory_path)

    # Loop through each file in the directory
    for file_name in file_list:
        # Check if the file is an Excel file
        if file_name.endswith('.xlsx'):
            # Construct the full path to the Excel file
            file_path = os.path.join(directory_path, file_name)

            # Read the Excel file into a DataFrame
            df = pd.read_excel(file_path)

            # Store the DataFrame in the dictionary using the file name as the key
            data_dict[file_name] = df

    return data_dict

def compare_product_sales(sales_data):
    """
    Compares the number of products sold for products that appear in multiple files.

    Args:
        sales_data (dict): A dictionary where keys are file names and values are DataFrames containing the sales data.

    Returns:
        dict: A dictionary containing product names as keys and their comparison results as values.
              Each comparison result includes the product name, average sales, and files where sales vary by more than 10% from the average.
    """
    product_sales = {}  # Dictionary to store product sales data

    # Iterate through each file in the sales_data dictionary
    for file_name, df in sales_data.items():
        # Iterate through the rows of the DataFrame
        for index, row in df.iterrows():
            product = row['Product']
            sold = row['Sold']

            # Check if the product is already in the product_sales dictionary
            if product in product_sales:
                # Update the product's sales data
                product_sales[product]['total_sales'] += sold
                product_sales[product]['file_count'] += 1
                product_sales[product]['sales_by_file'][file_name] = sold
            else:
                # Initialize the product's sales data
                product_sales[product] = {
                    'total_sales': sold,
                    'file_count': 1,
                    'sales_by_file': {file_name: sold}
                }

    # Calculate the average sales and identify files with sales more than 10% different from the average
    result = {}
    for product, data in product_sales.items():
        average_sales = data['total_sales'] / data['file_count']
        sales_by_file = data['sales_by_file']

        # Identify files where sales vary by more than 10% from the average
        varying_files = {}
        for file_name, sales in sales_by_file.items():
            if abs(sales - average_sales) / average_sales > 0.1:
                varying_files[file_name] = sales

        # Add the product to the result if there are varying files
        if varying_files:
            result[product] = {
                'average_sales': average_sales,
                'varying_files': varying_files
            }

    return result

# Example usage:
if __name__ == "__main__":
    directory_path = "sales"  # Replace with the path to your sales directory
    sales_data = read_sales_data(directory_path)
    comparison_result = compare_product_sales(sales_data)
    print(comparison_result)
    # Now, sales_data is a dictionary where each key is a file name, and each value is a DataFrame containing the data from that file.
    # You can access the data for a specific file like this:
    # data_for_file1 = sales_data["file1.xlsx"]
