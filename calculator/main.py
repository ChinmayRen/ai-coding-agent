# main.py

import sys
from pkg.calculator import Calculator
# from pkg.render import render  # Commenting out the render import


def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    expression = " ".join(sys.argv[1:])
    
    try:
        result = calculator.evaluate(expression)
        # to_print = render(expression, result)  # Commenting out the render call
        print(result)  # Printing the raw result
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()