import sys

lines = []

try:
    if (len(sys.argv) !=3): # making sure there are enough args
        sys.exit("format : python scourgify.py before.csv after.csv")
    before = sys.argv[1]
    after = sys.argv[2]

# making sure args are of format csv
    if not before.endswith(".csv") or (not after.endswith(".csv")) :
        sys.exit("file is not a csv file")

# opening file and putting all the content into a list
    with open(before) as file:
        #content = file.readlines()
        #for i in range(len(content)):
            #line = content[i]
            # if i == 0:
            #     name,house = line.strip().split(",")
            #     lines.append([name,house])
            # else:
            #     if (line != '\n') and (not line.isspace()):
            #         fname,lname,house = (line.rstrip().split(","))
            #         name = fname.removeprefix('"') + lname.removesuffix("\"")
            #         lines.append([name,house])

            # alternatively
        for line in file:
            line = line.strip().replace('"','')
            line = line.split(',')
            line = [x.strip() for x in line]
            lines.append(line)

        with open(after, "w") as file:
            file.write("first,last,house\n")
            for line in lines[1:]:
                str = line[1] + ","+ line[0] + "," + line[2] + "\n"
                file.write(str)
except FileNotFoundError:
    sys.exit("file doesn't exist")
