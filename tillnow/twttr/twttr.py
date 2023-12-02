str = input("Input: ")
vowels = ['a','e','i','o','u']
out = ""
for letter in str:
    if(letter.lower() not in vowels):
        out += letter
print(f"Output: {out}")