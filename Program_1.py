# Qn 1 :Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        if self.num2 == 0:
            return "Zero Division Error . Try Again"
        return self.num1 / self.num2



num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))



print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

calc = Calculator(num_1, num_2)
if choice == '1':
    print(f"The Sum is {calc.add()}")
elif choice == '2':
    print(f"The Difference is {calc.subtract()}")
elif choice == '3':
    print(f"The Product is {calc.multiply()}")
elif choice == '4':
    print(f"The Division result is {calc.divide()}")
else:
    print(f"Choose on of the 4 choices ")