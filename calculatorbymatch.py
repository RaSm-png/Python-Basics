x = float(input("What's x? "))
op = input("What you want to do? ")
y = float(input("What's y? "))


match op:
    case "+":
        print ("Addition of x & y is: ", x+y)
    case "-":
        print("Subtraction of x & Y is: ", x-y)
    case "*":
        print("Multiplicaton of x & Y is: ", x*y)
    case "/":
        if y==0:
            print("Invalid: Cannot divide by Zero")
        else:
            print("Devision of x & y is: ", x/y)
    case _:
        print("Invalid operator")


 