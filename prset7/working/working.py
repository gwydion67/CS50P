import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    if time := re.search(r"^([01]?[0-9])(:([0-5]?[0-9]))? ([AP]M) to ([01]?[0-9])(:([0-5]?[0-9]))? ([AP]M$)", s):
        if int(time[1]) < 1 or int(time[1]) > 12 or int(time[5]) < 1 or int(time[5]) > 12:
            raise ValueError('invalid time')

        frTime = standardTime(time[1], time[3] , time[4])
        toTime = standardTime(time[5] , time[7], time[8])

        return f"{frTime} to {toTime}"


    else:
        raise ValueError('invalid format')


def standardTime(hr,min,ampm):
    if hr == '12':
        if ampm == "AM":
            hour = '00'
        else:
            hour = '12'
    else:
        if ampm == 'AM':
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr) + 12}"
    if min == None:
        minute = '00'
    else:
        minute = f"{int(min):02}"
    return f"{hour}:{minute}"

if __name__ == "__main__":
    main()
