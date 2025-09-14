print("This is my calculator, please enter your three integers and I will multiply them!")

int1 = input("First Number:")
while int1.isnumeric() == False:
    int1 = input("Please try again, with an integer this time:")
int1 = float(int1)

int2 = input("Second Number:")
while int2.isnumeric() == False:
    int2 = input("Please try again, with an integer this time:")
int2 = float(int2)

int3 = input("Third Number:")
while int3.isnumeric() == False:
    int3 = input("Please try again, with an integer this time:")
int3 = float(int3)

print(input(int1 * int2 * int3))



