def main():
    time = input("What time is it? ")
    time = int(convert(time))

    if(time >= 7 and time <= 8):
        print("breakfast time")
    elif(time >= 12 and time <= 13):
        print("lunch time")
    elif(time >= 18 and time <= 19):
        print("dinner time")



def convert(time):
    time = time.strip().split(":")

    if(time[1].endswith('a.m.')):
        time[1] = time[1].removesuffix('a.m.').strip()
        hour = float(time[0])
    elif(time[1].endswith('p.m.')):
        time[1] = time[1].removesuffix('p.m.').strip()
        hour = (float(time[0]) + 12)
    else:
        hour = float(time[0])

    minute = float(time[1])/60

    return(hour + minute)




if __name__ == "__main__":
    main()