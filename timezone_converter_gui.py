import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

# Import the function to be used for time zone conversion
from timezone_converter import convert_timezone  # Replace with your actual module name

def convert_button_click():
    input_time_str = entry_input_time.get()
    from_timezone = combo_from_timezone.get()
    to_timezone = combo_to_timezone.get()

    try:
        # Parse the input time string to a datetime object
        input_time = datetime.strptime(input_time_str, "%Y-%m-%d %H:%M:%S")

        # Call the conversion function
        converted_time = convert_timezone(input_time, from_timezone, to_timezone)

        # Display the converted time in the output label
        label_output.config(text=f"Converted Time: {converted_time}")
    except ValueError:
        label_output.config(text="Invalid input time format")

# Create the main application window
root = tk.Tk()
root.title("Time Zone Converter")

# Create input widgets
label_input_time = tk.Label(root, text="Enter Date and Time (YYYY-MM-DD HH:MM:SS):")
entry_input_time = tk.Entry(root)
label_from_timezone = tk.Label(root, text="From Time Zone:")
combo_from_timezone = ttk.Combobox(root, values=pytz.all_timezones)
combo_from_timezone.set("UTC")  # Default value
label_to_timezone = tk.Label(root, text="To Time Zone:")
combo_to_timezone = ttk.Combobox(root, values=pytz.all_timezones)
combo_to_timezone.set("US/Pacific")  # Default value

# Create a convert button
convert_button = tk.Button(root, text="Convert", command=convert_button_click)

# Create an output label
label_output = tk.Label(root, text="Converted Time: ")

# Arrange the widgets using grid layout
label_input_time.grid(row=0, column=0, padx=10, pady=5)
entry_input_time.grid(row=0, column=1, padx=10, pady=5)
label_from_timezone.grid(row=1, column=0, padx=10, pady=5)
combo_from_timezone.grid(row=1, column=1, padx=10, pady=5)
label_to_timezone.grid(row=2, column=0, padx=10, pady=5)
combo_to_timezone.grid(row=2, column=1, padx=10, pady=5)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
label_output.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Start the main loop
root.mainloop()