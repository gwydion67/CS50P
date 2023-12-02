def main():
    frac = input("Fraction: ")
    left = convert(frac)
    f = gauge(left)
    print(f)


def convert(frac):
    part = frac.partition('/')
    if(not( part[0].isnumeric() and part[2].isnumeric())):
        raise ValueError
    if part[2] == '0':
        raise ZeroDivisionError
    left = round(100*int(part[0])/int(part[2]))
    if left > 100:
        raise ValueError
    return left

def gauge(left):
    if left <= 1:
        return("E")
    elif left >= 99:
        return("F")
    else:
        lef = str(left) + '%'
        return(lef)


if __name__ == "__main__":
    main()