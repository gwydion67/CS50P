import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if  nums := re.search(r"^([0-9]*)\.([0-9]*)\.([0-9]*)\.([0-9]*)$" , ip.strip()):
        if all(int(num) >= 0 and int(num) <= 255 for num in nums.groups()):
            return True
        else:
            return False
    else:
        return False



if __name__ == "__main__":
    main()