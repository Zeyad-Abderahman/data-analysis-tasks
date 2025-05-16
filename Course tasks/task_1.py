# ----------------------------------------------------------
# Task 1 - Temperature Conversion Tool
# Course: Intro to Data Analysis - Area Soft
# Instructor: Sayed Abdul-Monem
# Description:
# This program allows the user to convert temperatures
# between Celsius and Fahrenheit. After completing one
# conversion, the user will be prompted if they want to
# perform another.
# ----------------------------------------------------------

print("Hello user welcome to Task_1")

while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose (1/2): ") 

    if choice == '1':
        celsius = float(input("Enter Celsius: "))
        fahrenheit = celsius * 9/5 + 32
        print(f"Fahrenheit: {fahrenheit}")
    elif choice == '2':
        fahrenheit = float(input("Enter Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"Celsius: {celsius}")
    else:
        print("Invalid choice")

    repeat = input("Do you want to convert again? (yes/no): ").lower()
    if repeat != 'yes':
        break

print("Bye Bye user ❤")
