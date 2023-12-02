import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    if link := re.search(r"^<iframe src=\"https?://(www\.)?youtube\.com/embed/([\w+/?]+)\"></iframe>$" , s , re.IGNORECASE):
        return (f'https://youtu.be/{link.group(2)}')

if __name__ == "__main__":
    main()