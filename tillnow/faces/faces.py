def convert(string) :
    string = string.replace(":)","🙂").replace(":(","🙁")
    return string;

def main():
    a = input()
    a = convert(a)
    print(a)

main()