import random
while True:
    try:
        n = int(input("Level: "))
        if n > 0 :
            n = random.randint(1,n)
            break
    except:
        pass
while True:
    try:
        guess = int(input("Guess: "))
        if (guess > n):
            print("Too large!")
        elif (guess < n):
            print("Too small!")
        elif (guess == n):
            print("Just right!")
            break
    except:
        pass

