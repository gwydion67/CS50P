exp = input("Expression: ").lower().strip()
exp = exp.split()
x = float(exp[0]); y = exp[1]; z = float(exp[2]);
match y:
    case '+':
        print(x+z)
    case '-':
        print(x-z)
    case '*':
        print(x*z)
    case '/':
        print(x/z)