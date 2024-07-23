# Task 2 - Write a function that converts Fahreheit to Celsius.
def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
# Task 1, 3 - Take user input and use a try block to catch errors.
try:
    fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    if celsius is not None:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
except ValueError:
    print("Invalid input, please input a numeric value.")
# Task 4 - Use finally statement to thank user regardless of expcetion being caught or not.
finally:
    print("Thank you for using the weather forecast application!")
