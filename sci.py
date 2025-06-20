import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

class ScientificCalculator:
    def __init__(self):
        self.history = []

    def add_to_history(self, operation, result):
        self.history.append(f"{operation} = {result}")

    def basic_operations(self, num1, num2, op):
        operations = {
            "+": num1 + num2,
            "-": num1 - num2,
            "*": num1 * num2,
            "/": num1 / num2 if num2 != 0 else "Error: Division by zero",
            "^": math.pow(num1, num2)
        }
        result = operations.get(op, "Invalid operation")
        self.add_to_history(f"{num1} {op} {num2}", result)
        return result

    def advanced_functions(self, num, func):
        functions = {
            "sqrt": math.sqrt(num),
            "log": math.log(num),
            "exp": math.exp(num),
            "sin": math.sin(math.radians(num)),
            "cos": math.cos(math.radians(num)),
            "tan": math.tan(math.radians(num)),
            "factorial": math.factorial(int(num))
        }
        result = functions.get(func, "Invalid function")
        self.add_to_history(f"{func}({num})", result)
        return result

    def matrix_operations(self, matrix1, matrix2, op):
        operations = {
            "add": np.add(matrix1, matrix2),
            "subtract": np.subtract(matrix1, matrix2),
            "multiply": np.dot(matrix1, matrix2)
        }
        result = operations.get(op, "Invalid matrix operation")
        self.add_to_history(f"Matrix {op}", result)
        return result

    def solve_equation(self, equation):
        x = sp.Symbol('x')
        solution = sp.solve(equation, x)
        self.add_to_history(f"Solving {equation}", solution)
        return solution

    def differentiate(self, expression):
        x = sp.Symbol('x')
        derivative = sp.diff(expression, x)
        self.add_to_history(f"Differentiating {expression}", derivative)
        return derivative

    def integrate(self, expression):
        x = sp.Symbol('x')
        integral = sp.integrate(expression, x)
        self.add_to_history(f"Integrating {expression}", integral)
        return integral

    def plot_graph(self, expression):
        x = np.linspace(-10, 10, 400)
        y = [eval(expression.replace("x", str(val))) for val in x]
        plt.plot(x, y)
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title(f"Graph of {expression}")
        plt.grid()
        plt.show()

    def show_history(self):
        return "\n".join(self.history)

# Example usage
calc = ScientificCalculator()
print(calc.basic_operations(5, 3, "+"))
print(calc.advanced_functions(25, "sqrt"))
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print(calc.matrix_operations(matrix1, matrix2, "add"))
print(calc.solve_equation("x**2 - 4"))
print(calc.differentiate("x**3"))
print(calc.integrate("x**2"))
calc.plot_graph("x**(3)-8")
print("\nCalculation History:")
print(calc.show_history())