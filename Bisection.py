def f(x):
    # Define the function for which we want to find the root
    return x**2 - 5 # Example: f(x) = x^3 - x - 2


def bisection_method(a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None
    
    while (b - a) / 2.0 > epsilon:
        c = (a + b) / 2.0  # Midpoint
        if f(c) == 0:  # Found exact root
            return c
        elif f(a) * f(c) < 0:  # Root is in the left subinterval
            b = c
        else:  # Root is in the right subinterval
            a = c
    
    return (a + b) / 2.0  # Return the approximate root

# Main program
if __name__ == "__main__":
    a = float(input("Enter the lower bound (a): "))
    b = float(input("Enter the upper bound (b): "))
    epsilon_input = input("Enter the tolerance (epsilon) in decimal format (e.g., 0.0001 for 4 digits): ")
    epsilon = float(epsilon_input)
    
    root = bisection_method(a, b, epsilon)
    if root is not None:
        decimal_places = max(0, len(str(epsilon).split('.')[1])) # Get the number of decimal places
        print(f"The approximate root is: {root:.{decimal_places}f}")  # Print the result with specified decimal places