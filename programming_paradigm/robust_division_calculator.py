# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling.
    Handles:
    - Non-numeric input (ValueError)
    - Division by zero (ZeroDivisionError)
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is {result:.2f}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
