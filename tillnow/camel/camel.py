camel = input("camelCase: ")
snake = " "
for i in camel:
    if(i.islower()):
        snake += i
    else:
        snake += "_"
        snake += i.lower()
print(f"snake_case: {snake}")