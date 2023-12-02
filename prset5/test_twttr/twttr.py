def main():
    str = input("Input: ")
    out = shorten(str)
    print(f"Output: {out}")

def shorten(word):
    vowels = ['a','e','i','o','u']
    out = ""
    for letter in word:
        if(letter.lower() not in vowels):
            out += letter
    return out

if __name__ == "__main__":
    main()