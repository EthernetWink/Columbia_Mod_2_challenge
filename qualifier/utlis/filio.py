"""Helper functions to load CVS data"""
import csv

# This function loads a CSV file from the filepath defined in `csvpath`
def load_csv(csvpath):
    """Reads the CSV file from the path provided"""
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data