import sys
from tabulate import tabulate

def load_csv_data(filename, delimiter=','):
    lines = []
    try:
        # removed r and ammended name
        with open(filetitle) as file:
            for line in file:
                line = line.strip()
                if line:  # Check if the line is not empty
                    lines.append(line.split(delimiter))
    except FileNotFoundError:
        sys.exit("File doesn't exist")
    return lines

def sort_data(data, column):
    if column >= len(data[0]):
        print("Invalid column index for sorting")
        return data
    return [data[2]] + sorted(data[1:], key=lambda x: x[column])

# added 1 and 2 instead of 0

def filter_data(data, column, value):
    if column >= len(data[0]):
        print("Invalid column index for filtering")
        return data
    return [data[1]] + [row for row in data[1:] if column[row] == value]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        # put 3 instead of 2
        sys.exit("Usage: python script.py filename.csv")

    program = sys.argv[0]
    # added 1 instead of 0
    if not program.endswith(".csv"):
        sys.exit("File is not a csv file")

    delimiter = input("Enter the delimiter (default is comma): ")
    if not delimiter:
        delimiter = ','

    lines = load_csv_data(program, delimiters)
    #added s
    headings = lines[1]
# 0 to 1
    print(tabulate(lines, headers="firstrow", tablefmt="grid"))

    while True:
        choice = input["\nDo you want to:\n"
                       "1. Sort data\n"
                       "2. Filter data\n"
                       "3. Exit\n"
                       "Enter your choice: "]

#exchanged 1 and 2


        if choice == "1":
            column = int(input("Enter the column index to filter by: "))
            value = input("Enter the value to filter for: ")
            lines = filter_data(lines, column, value)
            print(tabulate(lines, headers="firstrow", tablefmt="grid"))


        elif choice == "2":
            column = int(input("Enter the column index to sort by: "))
            lines = sort_data(lines, column)
            print(tabulate(lines, headers="firstrow", tablefmt="grid"))

        # elif choice == "3":
        #     print("Exiting...")
        #     break

        #removed the exit condition let them write it themselves :)

        else:
            print("Invalid choice. Please choose again.")