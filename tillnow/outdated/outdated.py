months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if date[0].isalpha():
            date = date.split(", ")
            temp = date[0].split(" ")
            date.append(date[1])
            date[0] = temp[0]
            date[1] = temp[1]
        elif date.replace("/","").isnumeric():
            date = date.split("/")

        if date[1].isnumeric() and int(date[1]) <= 31:
            dd = int(date[1])
        if date[2].isnumeric():
            yyyy = int(date[2])
        if date[0].isnumeric() and int(date[0]) <= 12:
            mm = int(date[0])
        elif date[0].isalpha():
            mm = months.index(date[0]) + 1
        print(f"{yyyy:02d}-{mm:02d}-{dd:02d}")
        break
    except:
        pass


