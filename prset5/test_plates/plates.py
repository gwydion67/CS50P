def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if (not(( s[0].isalpha() and s[1].isalpha()))):
        return False

    firstnum = -1
    for i in range(2, len(s)):
        if not s[i].isalnum() :
            return False
    for i in range(2,len(s)):
        if s[i].isnumeric():
            firstnum = i
            break
    if firstnum > 0:
        if s[firstnum] == '0':
            return False
        if not s[firstnum:].isnumeric():
            return False
    return True

if __name__ == "__main__":
    main()