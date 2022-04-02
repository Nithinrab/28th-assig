import math


def recA (x, y):
    return x * y
def recP (x, y):
    return 2 * (x + y)
def circle(x):
    return math.pi * x * x
def square(x):
    return x * x
def tri(x, y, ):
    return (x * y) / 2
if __name__ == "__main__":
    print("1.Area of the rectangle.")
    print("2.Perimeter of the rectangle.")
    print("3.Area of the circle.")
    print("4.Area of the square.")
    print("5.Area of the triangle.")
    print("6.Exit.")
    c = int(input("Choose the option:"))

if c == 1:
    num1 = float(input("Enter the width of rectangle:"))
    num2 = float(input("Enter the length of rectangle:"))
    print("Area of the rectangle:", recA(num1, num2))

elif c == 2:
    num1 = float(input("Enter the length of rectangle:"))
    num2 = float(input("Enter the width of rectangle:"))
    print("Perimeter of rectangle:", recP(num1, num2))
elif c == 3:
    num1 = float(input("Enter the Radius of circle:"))
    print("Area of the circle:", circle(num1))
elif c == 4:
    num1 = float(input("Enter the side value of square:"))
    print("Area of sqaure is:", square(num1))
elif c == 5:
    num1 = float(input("Enter the base of triangle:"))
    num2 = float(input("Enter the height of triangle:"))
    print("Area of the triangle is:", tri(num1, num2))
elif c == 6:
    exit(6)

else:
    print("Invalid input.")


