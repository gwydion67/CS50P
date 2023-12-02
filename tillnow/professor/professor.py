import random
import sys

def main():
    level = get_level()
    score = int(0)
    for i in range(10):
        wrongs = int(0)
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == x+y:
                    if wrongs == 0:
                        score = score +1
                    break
                if ans != x+y:
                    wrongs = wrongs +1
                    print("EEE")
                if wrongs == 3:
                    print(f"{x} + {y} =",x+y)
                    break
            except ValueError:
                print("EEE")
            except:
                sys.exit()
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if (level == 1 or level == 2 or level == 3):
                return level
        except ValueError:
            pass
        except:
            sys.exit()


def generate_integer(level):
    if(level == 1):
        num = random.randint(0,9)
        return num

    fn = int(1)

    while (level-1):
        fn *= 10
        level -=1
    num = random.randint(fn , (fn*10 - 1))
    return num



if __name__ == "__main__":
    main()