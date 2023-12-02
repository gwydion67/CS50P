import sys

lines = []

try:
    if (len(sys.argv) < 2) or len(sys.argv) > 2:
        sys.exit("give 1 argumet only")
    program = sys.argv[1]
    if not program.endswith(".py"):
        sys.exit("file is not a python file")
    with open(program) as file:
        for line in file:
            if (not line.lstrip().startswith("#")) and (line != '\n') and (not line.isspace()):
                lines.append(line.rstrip())
except FileNotFoundError:
    sys.exit()
else:
    print(len(lines))