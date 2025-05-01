import unittest
from datetime import datetime
import pytz

# Import the function to be tested
from timezone_converter import convert_timezone  # Replace with your actual module name

class TestConvertTimezone(unittest.TestCase):

    def test_basic_conversion(self):
        input_time = datetime(2023, 9, 18, 12, 0, 0)
        from_timezone = 'UTC'
        to_timezone = 'US/Pacific'
        expected_output = datetime(2023, 9, 18, 5, 0, 0)  # Remove tzinfo for comparison
        result = convert_timezone(input_time, from_timezone, to_timezone)
        # Remove tzinfo from result for comparison
        result = result.replace(tzinfo=None)
        self.assertEqual(result, expected_output)

    def test_conversion_with_dst(self):
        input_time = datetime(2023, 3, 18, 12, 0, 0)
        from_timezone = 'UTC'
        to_timezone = 'US/Pacific'
        expected_output = datetime(2023, 3, 18, 5, 0, 0)  # Remove tzinfo for comparison
        result = convert_timezone(input_time, from_timezone, to_timezone)
        # Remove tzinfo from result for comparison
        result = result.replace(tzinfo=None)
        self.assertEqual(result, expected_output)

    def test_conversion_within_same_timezone(self):
        input_time = datetime(2023, 9, 18, 12, 0, 0)
        from_timezone = 'US/Pacific'
        to_timezone = 'US/Eastern'
        expected_output = datetime(2023, 9, 18, 15, 0, 0)  # Remove tzinfo for comparison
        result = convert_timezone(input_time, from_timezone, to_timezone)
        # Remove tzinfo from result for comparison
        result = result.replace(tzinfo=None)
        self.assertEqual(result, expected_output)

    def test_conversion_to_negative_offset_timezone(self):
        input_time = datetime(2023, 9, 18, 12, 0, 0)
        from_timezone = 'UTC'
        to_timezone = 'Asia/Kolkata'
        expected_output = datetime(2023, 9, 18, 17, 30, 0)  # Remove tzinfo for comparison
        result = convert_timezone(input_time, from_timezone, to_timezone)
        # Remove tzinfo from result for comparison
        result = result.replace(tzinfo=None)
        self.assertEqual(result, expected_output)

    def test_conversion_to_invalid_timezone(self):
        input_time = datetime(2023, 9, 18, 12, 0, 0)
        from_timezone = 'UTC'
        to_timezone = 'Invalid/Nonexistent'
        expected_output = "Invalid time zone provided"
        self.assertEqual(convert_timezone(input_time, from_timezone, to_timezone), expected_output)

    def test_conversion_with_erroneous_input_time(self):
        input_time = "Invalid Datetime Format"
        from_timezone = 'UTC'
        to_timezone = 'US/Pacific'
        expected_output = "Invalid input time"
        self.assertEqual(convert_timezone(input_time, from_timezone, to_timezone), expected_output)

    def test_conversion_with_erroneous_source_timezone(self):
        input_time = datetime(2023, 9, 18, 12, 0, 0)
        from_timezone = 'Invalid/Nonexistent'
        to_timezone = 'US/Pacific'
        expected_output = "Invalid time zone provided"
        self.assertEqual(convert_timezone(input_time, from_timezone, to_timezone), expected_output)

    def test_conversion_with_erroneous_target_timezone(self):
        input_time = datetime(2023, 9, 18, 12, 0, 0)
        from_timezone = 'UTC'
        to_timezone = 'Invalid/Nonexistent'
        expected_output = "Invalid time zone provided"
        self.assertEqual(convert_timezone(input_time, from_timezone, to_timezone), expected_output)

    def test_conversion_with_different_date(self):
        input_time = datetime(2023, 12, 25, 12, 0, 0)
        from_timezone = 'UTC'
        to_timezone = 'Australia/Sydney'
        expected_output = datetime(2023, 12, 25, 23, 0, 0)  # Remove tzinfo for comparison
        result = convert_timezone(input_time, from_timezone, to_timezone)
        # Remove tzinfo from result for comparison
        result = result.replace(tzinfo=None)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()