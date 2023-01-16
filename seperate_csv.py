import csv
import codecs
import os

# Define the directory where the output files will be saved
output_dir = "history_csv"

# Remove all CSV files in the directory
for file in os.listdir(output_dir):
    if file.endswith(".csv"):
        os.remove(os.path.join(output_dir, file))

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the input CSV file
with codecs.open('zetin_history.csv', 'r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file)
    output_file = None
    output_file_name = None
    for row in reader:
        # Check if the row is empty
        if not any(row):
            # Close the current output file if it is open
            if output_file:
                output_file.close()
            # Reset the output file variable
            output_file = None
            continue
        if not output_file:
            # Get the first 4 letter of the first line
            output_file_name = row[0]
            # remove last letter
            output_file_name = output_file_name[:-1]
            # Create a new output file with the name
            output_file = open(os.path.join(
                output_dir, f'{output_file_name}.csv'), 'w', newline='', encoding='utf-8')
            writer = csv.writer(output_file)
        writer.writerow(row)
    if output_file:
        output_file.close()
