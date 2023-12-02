names = []
while True:
    try:
        names.append(input(""))
    except EOFError:
        break
greet = "Adieu, adieu, to " + names[0]

if len(names) > 1:
    for name in names[1:-1]:
        greet = greet + ", " + name
    if len(names) > 2:
        greet = greet + ","
    greet = greet + " and " + names[-1]
print(greet)