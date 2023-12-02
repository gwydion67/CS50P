import sys
from tabulate import tabulate

lines = []

try:
    if (len(sys.argv) < 2) or len(sys.argv) > 2:
        sys.exit("give 1 argumet only")
    program = sys.argv[1]
    if not program.endswith(".csv"):
        sys.exit("file is not a csv file")
    with open(program) as file:
        for line in file:
            if (line != '\n') and (not line.isspace()):
                #print(line)
                #row = line.rstrip().split(",")
                lines.append(line.rstrip().split(","))
except FileNotFoundError:
    sys.exit("file doesn't exist")
else:
    headings = lines[0]
    #print(lines)
    print(tabulate(lines, headers = "firstrow" , tablefmt="grid"))
