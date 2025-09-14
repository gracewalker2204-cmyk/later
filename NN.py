print("This is my calculator, if you are a rat please enter your three numbers and I will multiply them!")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except Exception as e:
            print("Please try again, with a valid number.")
            print(e)

int1 = get_number("First Number: ")
int2 = get_number("Second Number: ")
int3 = get_number("Third Number: ")

result = int1 * int2 * int3


if abs(result) >= 1e6 or (0 < abs(result) < 1e-3):

    print(f"The result is: {result:.5e}")
else:

    print(f"The result is: {result:.5f}")