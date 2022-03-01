def greeting(name):
    print('Hello', name)
greeting(input('Enter your name\n'))

def addition(num1,num2):
    return num1 + num2

def main():
    num1 = float(input('Enter your first number:\n'))
    num2 = float(input('Enter your second number:\n'))

    result = addition(num1,num2)
    print(f"{num1} + {num2} = {result}")

main()