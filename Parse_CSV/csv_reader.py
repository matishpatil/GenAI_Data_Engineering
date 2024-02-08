import csv
import random
import sys

def sample_csv_rows(input_file, sample_size=10):
    with open(input_file, 'r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Assuming the first row contains headers
        rows = list(reader)
        sampled_rows = random.sample(rows, min(sample_size, len(rows)))
        return headers, sampled_rows

def main():
    if len(sys.argv) != 2:
        print("Usage: python sample_csv.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        headers, sampled_rows = sample_csv_rows(input_file)
        print("Sampled Rows:")
        print(headers)
        for row in sampled_rows:
            print(row)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()