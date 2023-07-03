import os
import csv

# Specify the folder path where the CSV files are located
folder_path = "./agreements"

# Initialize an empty list to store the CSV files
serial_numbers = []

# Loop through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):  # Check if the file is a CSV file
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row if it exists
            for row in reader:
                serial_number = row[0]
                serial_numbers.append(f"{file_name}, {serial_number}")

print(f"Total serial numbers loaded: {len(serial_numbers)}")