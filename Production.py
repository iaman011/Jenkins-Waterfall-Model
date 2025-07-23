print("Hello! This is a Production Stage")
from Test import add, subtract, multiply, divide

def main():
    a = 10
    b = 20

    print("Production Calculator Run")
    print("--------------------------")
    print(f"Add: {a} + {b} = {add(a, b)}")
    print(f"Sub: {a} - {b} = {subtract(a, b)}")
    print(f"Mul: {a} * {b} = {multiply(a, b)}")
    print(f"Div: {a} / {b} = {divide(a, b)}")

if __name__ == '__main__':
    main()
