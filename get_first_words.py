def extract_first_words(input_file, output_file, delimiter=','):
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            parts = line.strip().split(delimiter)
            if parts:  # Make sure the line is not empty
                outfile.write(parts[0] + '\n')

if __name__ == "__main__":
    input_file = input("Enter the input file name (e.g., files/input.txt): ").strip()
    output_file = input("Enter the output file name (e.g., files/output.txt): ").strip()
    delimiter = input("Enter the delimiter (default is ','): ").strip()
    delimiter = delimiter if delimiter else ','

    try:
        extract_first_words(input_file, output_file, delimiter)
        print(f"First words extracted and saved to '{output_file}'.")
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
