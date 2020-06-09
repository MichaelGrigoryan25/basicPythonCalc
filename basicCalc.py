operators = ["/", "+", "*", "-"]
def getNums():
    x = float(input("X: "))
    operator = input(operators)
    y = float(input("Y: "))
    sum = str("Is this the right expression? " + str(x) + " " + operator + " " + str(y) + ": ")
    sumAnswer = input(sum + "[Y/N]")
    def calc():
        if operator == operators[0]:
            print(x/y)
        elif operator == operators[1]:
            print(x+y)
        elif operator == operators[2]:
            print(x*y)
        elif operator == operators[3]:
            print(x-y)
    if sum == "Y":
        calc()
    elif sum == "N":
        getNums()
    else:
        print("Error")
        print("Please start again.")
        getNums()
getNums()
