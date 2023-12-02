grocery = {}
while True:
    try:
        item = (input().upper())
        if item in grocery:
            grocery[item] += int(1);
        else:
            grocery[item] = int(1)
    except EOFError:
        break
    except:
        pass
items = list(grocery.keys())
items.sort()
grocery = {i: grocery[i] for i in items}
for item in grocery :
    print(grocery[item],item)

