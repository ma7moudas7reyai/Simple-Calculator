OPERATIONS = {
    "+": lambda left, right: left + right,
    "-": lambda left, right: left - right,
    "*": lambda left, right: left * right,
    "/": lambda left, right: left / right,
    "%": lambda left, right: left % right,
}


def calculate(left, right, operator):
    """Calculate a result for one of the supported arithmetic operators."""
    if operator not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {operator}")
    if operator in {"/", "%"} and right == 0:
        raise ZeroDivisionError("The second number cannot be zero for this operation.")
    return OPERATIONS[operator](left, right)


def main():
    print("Simple Calculator")
    while True:
        try:
            left = float(input("First number: "))
            operator = input("Operation (+, -, *, /, %): ").strip()
            right = float(input("Second number: "))
            print(f"Result: {calculate(left, right, operator):g}")
        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")

        if input("Another calculation? (y/n): ").strip().lower() != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
