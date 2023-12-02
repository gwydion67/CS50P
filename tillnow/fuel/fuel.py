while True:
    frac = input("Fraction: ")
    part = frac.partition('/')
    try:
        left = round(100*int(part[0])/int(part[2]))
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        if(left <= 100):
            if left <= 1:
                print("E")
            elif left >= 99:
                print("F")
            else:
                print(left,"%",sep ="")
            break



