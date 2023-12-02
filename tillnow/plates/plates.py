def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if (not s[0].isalpha() and not s[1].isalpha()):
        return False
    for i in range(2, len(s)):
        if not s[i].isalnum() :
            return False
        if s[i].isnumeric():
            if not s[i:].isnumeric():
                return False
            if s[i] == '0':
                return False
    return True


main()