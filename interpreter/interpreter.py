def main():
    expression=input("Expression: ")
    interpret(expression)
    print(float(interpret(expression)))

def interpret(expression):
    x, y, z = expression.split(" ")
    x=int(x)
    z=int(z)
    if y=="+":
        return(x+z)
    elif y=="-":
        return(x-z)
    elif y=="*":
        return (x*z)
    elif y=="/":
        return (x/z)


main()
