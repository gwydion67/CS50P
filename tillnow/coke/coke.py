total = int(0)
due = int(50)

while total < 50 :
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    if (coin == 5 or coin == 10 or coin == 25):
        total = total + coin
        due = due - coin

if due == 0 :
    print("Change Owed: 0")
else:
    due = -1 * due
    print(f"Change Owed: {due}")