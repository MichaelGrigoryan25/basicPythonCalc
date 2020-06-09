operators = ["/", "+", "*", "-", "%", "**"]
dots = str("." * 30)

def getNums():
    print(dots)
    x = float(input("X: "))
    print(dots)
    operator = input(operators)
    print(dots)
    y = float(input("Y: "))
    print(dots)
    sum = str("Is this the right expression? " + str(x) + " " + operator + " " + str(y) + ": ")
    sumAnswer = input(sum + "[Y/N]: ")
    def calc():
        print("The answer is")
        if operator == operators[0]:
            print(x/y)
        elif operator == operators[1]:
            print(x+y)
        elif operator == operators[2]:
            print(x*y)
        elif operator == operators[3]:
            print(x-y)
        elif operator == operators[4]:
            print(x%y)
        elif operator == operators[5]:
            print(x**y)
    if sumAnswer == "Y":
        calc()
    elif sumAnswer == "N":
        getNums()
    else:
        print("Error\nPlease start again.")
        getNums()
getNums()
