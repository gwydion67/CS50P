import re
import sys


def main():
    print(count(input("Text: ")))


def count(str):
    count = 0
    # str = str.strip().split(' ')
    # for s in str:
    #     if match := re.search(r"^um[^\w]*$", s, flags=re.I):
    #         count = count + 1
    if match := re.findall(r"\bum\b", str, flags=re.I):
        count = len(match)
    return count



if __name__ == "__main__":
    main()
