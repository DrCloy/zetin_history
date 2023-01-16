import csv
import codecs

# Open the input CSV file and create a new output CSV file
with codecs.open('zetin_history_all.csv', 'r', encoding='utf-8') as input_file, open('zetin_history.csv', 'w', newline='', encoding='utf-8') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Iterate over each row in the input CSV
    for row in reader:
        # Remove the last column from the row
        row = row[:-1]

        # Write the modified row to the output CSV
        writer.writerow(row)
