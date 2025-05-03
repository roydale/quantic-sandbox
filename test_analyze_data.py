import unittest
import pandas as pd
import os

# Import the function you want to test
from analyze_data import read_sales_data  # Replace 'your_module' with the actual name of your Python module

class TestReadSalesData(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing and generate some test Excel files
        self.test_dir = "test_sales"
        os.makedirs(self.test_dir, exist_ok=True)
        self.create_test_files()

    def create_test_files(self):
        # Create two test Excel files with sample data
        data1 = {'Product': ['A', 'B', 'C'], 'Sold': [10, 20, 30]}
        data2 = {'Product': ['X', 'Y', 'Z'], 'Sold': [5, 15, 25]}
        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)
        df1.to_excel(os.path.join(self.test_dir, 'test_file1.xlsx'), index=False)
        df2.to_excel(os.path.join(self.test_dir, 'test_file2.xlsx'), index=False)

    def tearDown(self):
        # Remove the temporary test files
        for file_name in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file_name)
            os.remove(file_path)

        # Remove the temporary test directory
        os.rmdir(self.test_dir)
    
    def test_read_sales_data(self):
        # Test reading data from test files
        data_dict = read_sales_data(self.test_dir)

        # Check if the correct number of files are read
        self.assertEqual(len(data_dict), 2)

        # Check if the data for each file is correctly read into a DataFrame
        self.assertTrue('test_file1.xlsx' in data_dict)
        self.assertTrue('test_file2.xlsx' in data_dict)

        # Check if the data in the DataFrames is as expected
        self.assertTrue(data_dict['test_file1.xlsx'].equals(pd.DataFrame({'Product': ['A', 'B', 'C'], 'Sold': [10, 20, 30]})))
        self.assertTrue(data_dict['test_file2.xlsx'].equals(pd.DataFrame({'Product': ['X', 'Y', 'Z'], 'Sold': [5, 15, 25]})))

if __name__ == '__main__':
    unittest.main()
